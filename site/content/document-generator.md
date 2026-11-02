title: Document Generator
section: Sales
order: 0
---
# Deal Document Generator

Create a working draft of an SLA, RFP & Brand Brief, or SOW / Order Form without editing the source documents. Everything runs in this browser: nothing is uploaded or saved to a server. Review all generated documents with counsel before sending.

<div class="generator" id="document-generator">
  <section class="generator-panel" aria-label="Document fields">
    <h2>Deal details</h2>
    <div class="field">
      <label for="document-type">Document type</label>
      <select id="document-type">
        <option value="sla">SLA</option>
        <option value="rfp">RFP &amp; Brand Brief</option>
        <option value="sow">SOW / Order Form</option>
      </select>
    </div>
    <div class="field-grid">
      <div class="field">
        <label for="company-name">Company legal name</label>
        <input id="company-name" placeholder="Acme, Inc.">
      </div>
      <div class="field">
        <label for="brand-name">Brand / product</label>
        <input id="brand-name" placeholder="Acme Coffee">
      </div>
    </div>
    <div class="field-grid">
      <div class="field">
        <label for="contact-name">Primary contact</label>
        <input id="contact-name" placeholder="Name, title">
      </div>
      <div class="field">
        <label for="contact-email">Contact email</label>
        <input id="contact-email" type="email" placeholder="name@company.com">
      </div>
    </div>
    <div class="field-grid">
      <div class="field">
        <label for="effective-date">Effective / issue date</label>
        <input id="effective-date" type="date">
      </div>
      <div class="field">
        <label for="end-date">Term end / response due</label>
        <input id="end-date" type="date">
      </div>
    </div>
    <div class="field">
      <label for="price-agreement">Price agreement</label>
      <input id="price-agreement" placeholder="$25,000 sponsorship + $1,500 implementation">
    </div>
    <div class="field">
      <label for="placements">Placements / scope</label>
      <textarea id="placements" placeholder="Branded throwable on all maps; two interactive props"></textarea>
    </div>
    <div class="field">
      <label for="additional-terms">Additional terms</label>
      <textarea id="additional-terms" placeholder="Exclusivity, approval windows, reporting, co-marketing..."></textarea>
    </div>
    <div class="field">
      <label for="amendments">Amendments / change notes</label>
      <textarea id="amendments" placeholder="Changes to the standard draft or agreed exceptions..."></textarea>
    </div>
    <div id="sow-fields">
      <div class="field">
        <label>Scope line items</label>
        <div class="line-items" id="line-items"></div>
        <button class="add-line" type="button" id="add-line">+ Add placement</button>
        <p class="helper">Add a placement and its agreed fee. Remove unused rows.</p>
      </div>
      <div class="field">
        <label for="payment-schedule">Payment schedule</label>
        <input id="payment-schedule" value="Implementation fee + 50% of sponsorship fee at signing; 50% at Go-Live; Net 30.">
      </div>
    </div>
    <div class="generator-actions">
      <button type="button" id="print-document">Print / Save PDF</button>
      <button type="button" class="secondary" id="download-document">Download .txt</button>
      <button type="button" class="secondary" id="reset-document">Reset</button>
    </div>
  </section>
  <section class="preview-panel" aria-live="polite">
    <h2>Live draft</h2>
    <p class="preview-meta">Edit any field to update the draft. Use Print / Save PDF when it is ready for review.</p>
    <article class="document-preview" id="document-preview"></article>
  </section>
</div>

<script>
(function () {
  "use strict";
  var root = document.getElementById("document-generator");
  if (!root) return;
  var ids = ["document-type", "company-name", "brand-name", "contact-name", "contact-email",
    "effective-date", "end-date", "price-agreement", "placements", "additional-terms", "amendments",
    "payment-schedule"];
  var fields = {};
  ids.forEach(function (id) { fields[id] = document.getElementById(id); });
  var lineItems = document.getElementById("line-items");
  var preview = document.getElementById("document-preview");
  var sowFields = document.getElementById("sow-fields");

  function escapeHtml(text) {
    return String(text).replace(/[&<>"']/g, function (character) {
      return {"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"}[character];
    });
  }
  function value(id, fallback) {
    var current = fields[id] && fields[id].value.trim();
    return escapeHtml(current || fallback || "[Not specified]");
  }
  function dateValue(id, fallback) {
    var current = value(id, fallback);
    if (current === "[Not specified]") return current;
    var parsed = new Date(current + "T00:00:00");
    return isNaN(parsed.getTime()) ? current : parsed.toLocaleDateString();
  }
  function addLine(name, fee) {
    var row = document.createElement("div");
    row.className = "line-item";
    row.innerHTML = '<input class="line-name" aria-label="Placement name" placeholder="Placement or deliverable">' +
      '<input class="line-fee" aria-label="Placement fee" placeholder="$ fee">' +
      '<button type="button" aria-label="Remove placement">×</button>';
    row.querySelector(".line-name").value = name || "";
    row.querySelector(".line-fee").value = fee || "";
    row.querySelector("button").addEventListener("click", function () {
      row.remove();
      update();
    });
    row.querySelector(".line-name").addEventListener("input", update);
    row.querySelector(".line-fee").addEventListener("input", update);
    lineItems.appendChild(row);
  }
  function getLines() {
    return Array.prototype.slice.call(lineItems.querySelectorAll(".line-item")).map(function (row) {
      return escapeHtml(row.querySelector(".line-name").value.trim() || "[Placement]") + " — " +
        escapeHtml(row.querySelector(".line-fee").value.trim() || "[Fee]");
    });
  }
  function block(label, text) {
    return '<div class="doc-section">' + label + '</div><div>' + text.replace(/\n/g, "<br>") + '</div>';
  }
  function renderSla() {
    return '<div class="doc-kicker">Blind Sight · Schedule B</div>' +
      '<h3>Service Level Agreement</h3>' +
      '<div>Between Kato.8 Studios LLC ("Studio") and ' + value("company-name", "[Sponsor]") + ' ("Sponsor"). Effective ' +
      dateValue("effective-date", "[date]") + ' through ' + dateValue("end-date", "[term end]") + '.</div>' +
      block("1. Service scope", value("placements", "Placement availability, delivery, revisions, go-live confirmation, and reporting as agreed in the Order Form.")) +
      block("2. Commercial agreement", value("price-agreement", "[Sponsorship fee and implementation fee]")) +
      block("3. Sponsor commitments", "Sponsor supplies complete brand assets, approvals, and payments on time. Named contact: " +
        value("contact-name", "[name]") + " (" + value("contact-email", "[email]") + ").") +
      block("4. Additional terms", value("additional-terms", "Studio will provide launch and quarterly reporting. Service credits, if any, are limited to the agreed sponsorship fee period.")) +
      block("5. Amendments", value("amendments", "No amendments.")) +
      '<div class="doc-section">Signatures</div><div>Studio: Terry Teng, Kato.8 Studios LLC<br>Sponsor: ' +
      value("company-name", "[Sponsor]") + '</div>';
  }
  function renderRfp() {
    return '<div class="doc-kicker">Blind Sight · Sales</div>' +
      '<h3>Sponsorship RFP &amp; Brand Brief</h3>' +
      '<div><strong>Issued by:</strong> Kato.8 Studios LLC · <strong>Issued:</strong> ' +
      dateValue("effective-date", "[date]") + ' · <strong>Responses due:</strong> ' + dateValue("end-date", "[date]") + '</div>' +
      block("1. The opportunity", "Blind Sight is a 4–8 player asymmetric horror-comedy for PC (Steam). Kato.8 Studios is offering a limited number of founding brand partners a place inside the game.") +
      block("2. Brand / product", value("brand-name", "[Brand / product]") + " for " + value("company-name", "[Company legal name]") + ".") +
      block("3. Requested scope", value("placements", "Placements of interest, preferred term, exclusivity, and campaign goals.")) +
      block("4. Budget / price agreement", value("price-agreement", "[Budget range or agreed pricing]")) +
      block("5. Contact", value("contact-name", "[Primary contact]") + " · " + value("contact-email", "[Email]")) +
      block("6. Additional terms", value("additional-terms", "Please include brand restrictions, mandatory legal lines, approval steps, and co-marketing commitments.")) +
      block("7. Amendments / notes", value("amendments", "No amendments.")) +
      '<div class="doc-section">Non-binding notice</div><div>This RFP is not an offer and creates no obligation. Proposals and discussions are confidential. A binding deal requires signed definitive agreements.</div>';
  }
  function renderSow() {
    var lines = getLines().map(function (line, index) { return (index + 1) + ". " + line; }).join("<br>");
    return '<div class="doc-kicker">Blind Sight · Order Form</div>' +
      '<h3>Statement of Work / Order Form</h3>' +
      '<div>Between Kato.8 Studios LLC ("Studio") and ' + value("company-name", "[Sponsor]") + ' ("Sponsor"). Effective ' +
      dateValue("effective-date", "[date]") + ' through ' + dateValue("end-date", "[term end]") + '.</div>' +
      block("A. Order details", "Sponsor contact: " + value("contact-name", "[name]") + " · " + value("contact-email", "[email]") +
        "<br>Brand / product: " + value("brand-name", "[Brand]") + "<br>Scope: " + value("placements", "[Placements and maps]")) +
      block("B. Placements and fees", lines || "[Add placement line items]") +
      block("C. Price and payment", value("price-agreement", "[Sponsorship fee + implementation fee]") + "<br>" +
        value("payment-schedule", "[Payment schedule]")) +
      block("D. Studio deliverables", "Concept or mockup, production-ready assets, sponsor-slot integration, approval submission, Go-Live confirmation, and reporting.") +
      block("E. Additional terms", value("additional-terms", "Two approval rounds are included. Extra maps, products, animation, or live-ops content require a change order.")) +
      block("F. Amendments / change notes", value("amendments", "No amendments.")) +
      '<div class="doc-section">Signatures</div><div>Studio: Terry Teng, Kato.8 Studios LLC<br>Sponsor: ' +
      value("company-name", "[Sponsor]") + '</div>';
  }
  function plainText() {
    var clone = preview.cloneNode(true);
    return clone.textContent.replace(/\n{3,}/g, "\n\n").trim() + "\n";
  }
  function update() {
    var type = fields["document-type"].value;
    sowFields.style.display = type === "sow" ? "block" : "none";
    preview.innerHTML = type === "sla" ? renderSla() : type === "rfp" ? renderRfp() : renderSow();
  }
  ids.forEach(function (id) { fields[id].addEventListener("input", update); fields[id].addEventListener("change", update); });
  document.getElementById("add-line").addEventListener("click", function () { addLine(); update(); });
  document.getElementById("print-document").addEventListener("click", function () { window.print(); });
  document.getElementById("download-document").addEventListener("click", function () {
    var blob = new Blob([plainText()], { type: "text/plain;charset=utf-8" });
    var link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = (value("company-name", "blind-sight") + "-" + fields["document-type"].value + ".txt").toLowerCase().replace(/[^a-z0-9]+/g, "-");
    link.click();
    URL.revokeObjectURL(link.href);
  });
  document.getElementById("reset-document").addEventListener("click", function () {
    ids.forEach(function (id) { if (id !== "document-type") fields[id].value = ""; });
    fields["document-type"].value = "sla";
    lineItems.innerHTML = "";
    addLine("Branded placement", "");
    update();
  });
  addLine("Branded placement", "");
  update();
}());
</script>
