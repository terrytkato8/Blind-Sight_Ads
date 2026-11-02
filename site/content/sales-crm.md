title: Sales CRM
section: Sales
order: 1
---
# Sales & Client CRM

Track prospective sponsors and active clients alongside the deal documents. Records are saved in this browser only. Use **Export backup** regularly and keep the JSON file somewhere secure; importing replaces the current browser data.

<div class="crm-app" id="sales-crm">
  <section class="crm-toolbar" aria-label="CRM controls">
    <div>
      <label class="sr-only" for="crm-search">Search clients</label>
      <input id="crm-search" placeholder="Search company, contact, notes...">
    </div>
    <div class="crm-actions">
      <button type="button" id="new-client">+ New client</button>
      <button type="button" class="secondary" id="export-crm">Export backup</button>
      <button type="button" class="secondary" id="import-crm">Import backup</button>
      <input type="file" id="import-file" accept="application/json" hidden>
    </div>
  </section>
  <section class="crm-summary" id="crm-summary"></section>
  <div class="crm-layout">
    <section class="crm-list-panel">
      <div class="crm-list-heading">
        <h2>Pipeline</h2>
        <select id="stage-filter" aria-label="Filter by pipeline stage">
          <option value="all">All stages</option>
          <option>Lead</option>
          <option>Qualified</option>
          <option>Proposal</option>
          <option>Negotiation</option>
          <option>Won</option>
          <option>Lost</option>
        </select>
      </div>
      <div id="client-list" class="client-list"></div>
    </section>
    <section class="crm-editor-panel">
      <div id="empty-editor" class="crm-empty">
        <h2>Build your pipeline</h2>
        <p>Create a client record to track contacts, pricing, next steps, and the documents you generate for each opportunity.</p>
        <button type="button" id="empty-new-client">Create first client</button>
      </div>
      <form id="client-editor" hidden>
        <div class="editor-heading">
          <div>
            <p class="eyebrow">Client record</p>
            <h2 id="editor-title">New client</h2>
          </div>
          <button type="button" class="danger-button" id="delete-client">Delete</button>
        </div>
        <div class="crm-field-grid">
          <div class="field"><label for="client-company">Company</label><input id="client-company" required placeholder="Acme, Inc."></div>
          <div class="field"><label for="client-contact">Primary contact</label><input id="client-contact" placeholder="Name, title"></div>
          <div class="field"><label for="client-email">Email</label><input id="client-email" type="email" placeholder="name@company.com"></div>
          <div class="field"><label for="client-stage">Stage</label><select id="client-stage"><option>Lead</option><option>Qualified</option><option>Proposal</option><option>Negotiation</option><option>Won</option><option>Lost</option></select></div>
          <div class="field"><label for="client-value">Estimated deal value (USD)</label><input id="client-value" type="number" min="0" step="100" placeholder="25000"></div>
          <div class="field"><label for="client-next-date">Next action date</label><input id="client-next-date" type="date"></div>
          <div class="field crm-wide"><label for="client-next-action">Next action</label><input id="client-next-action" placeholder="Send sponsor term sheet"></div>
          <div class="field crm-wide"><label for="client-scope">Opportunity / placements</label><textarea id="client-scope" placeholder="Branded throwable, interactive prop, title sponsor..."></textarea></div>
          <div class="field crm-wide"><label for="client-notes">Notes</label><textarea id="client-notes" placeholder="Budget, decision process, brand restrictions, follow-ups..."></textarea></div>
        </div>
        <div class="crm-form-actions"><button type="submit">Save client</button><button type="button" class="secondary" id="cancel-edit">Cancel</button></div>
      </form>
    </section>
  </div>
</div>

<script>
(function () {
  "use strict";
  var app = document.getElementById("sales-crm");
  if (!app) return;
  var STORAGE_KEY = "blind-sight-sales-crm-v1";
  var stages = ["Lead", "Qualified", "Proposal", "Negotiation", "Won", "Lost"];
  var records = [];
  var selectedId = null;
  var search = document.getElementById("crm-search");
  var stageFilter = document.getElementById("stage-filter");
  var list = document.getElementById("client-list");
  var summary = document.getElementById("crm-summary");
  var editor = document.getElementById("client-editor");
  var empty = document.getElementById("empty-editor");
  var formFields = {
    company: document.getElementById("client-company"),
    contact: document.getElementById("client-contact"),
    email: document.getElementById("client-email"),
    stage: document.getElementById("client-stage"),
    value: document.getElementById("client-value"),
    nextDate: document.getElementById("client-next-date"),
    nextAction: document.getElementById("client-next-action"),
    scope: document.getElementById("client-scope"),
    notes: document.getElementById("client-notes")
  };
  function escapeHtml(text) {
    return String(text || "").replace(/[&<>"']/g, function (character) {
      return {"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"}[character];
    });
  }
  function load() {
    try {
      var saved = JSON.parse(localStorage.getItem(STORAGE_KEY) || "[]");
      records = Array.isArray(saved) ? saved : [];
    } catch (error) {
      records = [];
    }
  }
  function save() {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(records));
  }
  function money(amount) {
    return Number(amount || 0).toLocaleString(undefined, {style: "currency", currency: "USD", maximumFractionDigits: 0});
  }
  function dateLabel(date) {
    if (!date) return "No next action date";
    var parsed = new Date(date + "T00:00:00");
    return isNaN(parsed.getTime()) ? date : parsed.toLocaleDateString();
  }
  function filteredRecords() {
    var query = search.value.trim().toLowerCase();
    return records.filter(function (record) {
      var matchesStage = stageFilter.value === "all" || record.stage === stageFilter.value;
      var haystack = [record.company, record.contact, record.email, record.scope, record.notes, record.nextAction].join(" ").toLowerCase();
      return matchesStage && (!query || haystack.indexOf(query) !== -1);
    }).sort(function (a, b) { return (a.nextDate || "9999").localeCompare(b.nextDate || "9999"); });
  }
  function renderSummary() {
    var active = records.filter(function (record) { return record.stage !== "Lost" && record.stage !== "Won"; });
    var pipeline = active.reduce(function (total, record) { return total + Number(record.value || 0); }, 0);
    var won = records.filter(function (record) { return record.stage === "Won"; }).reduce(function (total, record) { return total + Number(record.value || 0); }, 0);
    summary.innerHTML = '<div><strong>' + records.length + '</strong><span>Total clients</span></div>' +
      '<div><strong>' + money(pipeline) + '</strong><span>Open pipeline</span></div>' +
      '<div><strong>' + money(won) + '</strong><span>Won value</span></div>' +
      '<div><strong>' + active.filter(function (record) { return record.nextDate && record.nextDate < new Date().toISOString().slice(0, 10); }).length + '</strong><span>Overdue actions</span></div>';
  }
  function renderList() {
    var visible = filteredRecords();
    list.innerHTML = visible.length ? visible.map(function (record) {
      return '<button type="button" class="client-card' + (record.id === selectedId ? " selected" : "") + '" data-id="' + escapeHtml(record.id) + '">' +
        '<span class="client-card-top"><strong>' + escapeHtml(record.company || "Unnamed client") + '</strong><span class="stage-pill stage-' + record.stage.toLowerCase() + '">' + escapeHtml(record.stage) + '</span></span>' +
        '<span class="client-card-contact">' + escapeHtml(record.contact || "No contact") + '</span>' +
        '<span class="client-card-bottom"><span>' + money(record.value) + '</span><span>' + escapeHtml(record.nextAction || dateLabel(record.nextDate)) + '</span></span></button>';
    }).join("") : '<div class="no-records">No matching clients yet.<br><button type="button" id="no-records-new">Add a client</button></div>';
    list.querySelectorAll("[data-id]").forEach(function (button) {
      button.addEventListener("click", function () { select(button.getAttribute("data-id")); });
    });
    var emptyButton = document.getElementById("no-records-new");
    if (emptyButton) emptyButton.addEventListener("click", newClient);
  }
  function render() {
    renderSummary();
    renderList();
    if (selectedId) {
      var selected = records.find(function (record) { return record.id === selectedId; });
      if (selected) {
        empty.hidden = true;
        editor.hidden = false;
        document.getElementById("editor-title").textContent = selected.company || "Edit client";
        Object.keys(formFields).forEach(function (key) { formFields[key].value = selected[key] || ""; });
        return;
      }
    }
    empty.hidden = false;
    editor.hidden = true;
  }
  function select(id) {
    selectedId = id;
    render();
  }
  function newClient() {
    var id = "client-" + Date.now();
    records.push({id: id, company: "", contact: "", email: "", stage: "Lead", value: "", nextDate: "", nextAction: "", scope: "", notes: ""});
    selectedId = id;
    save();
    render();
    formFields.company.focus();
  }
  editor.addEventListener("submit", function (event) {
    event.preventDefault();
    var record = records.find(function (item) { return item.id === selectedId; });
    if (!record) return;
    Object.keys(formFields).forEach(function (key) { record[key] = formFields[key].value.trim(); });
    save();
    render();
  });
  document.getElementById("new-client").addEventListener("click", newClient);
  document.getElementById("empty-new-client").addEventListener("click", newClient);
  document.getElementById("cancel-edit").addEventListener("click", function () { selectedId = null; render(); });
  document.getElementById("delete-client").addEventListener("click", function () {
    if (!selectedId || !window.confirm("Delete this client record?")) return;
    records = records.filter(function (record) { return record.id !== selectedId; });
    selectedId = null;
    save();
    render();
  });
  search.addEventListener("input", renderList);
  stageFilter.addEventListener("change", renderList);
  document.getElementById("export-crm").addEventListener("click", function () {
    var blob = new Blob([JSON.stringify(records, null, 2)], {type: "application/json"});
    var link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "blind-sight-sales-crm-" + new Date().toISOString().slice(0, 10) + ".json";
    link.click();
    URL.revokeObjectURL(link.href);
  });
  document.getElementById("import-crm").addEventListener("click", function () { document.getElementById("import-file").click(); });
  document.getElementById("import-file").addEventListener("change", function (event) {
    var file = event.target.files[0];
    if (!file) return;
    var reader = new FileReader();
    reader.onload = function () {
      try {
        var imported = JSON.parse(reader.result);
        if (!Array.isArray(imported)) throw new Error("Backup must be an array.");
        records = imported;
        selectedId = null;
        save();
        render();
      } catch (error) {
        window.alert("Could not import that backup. Please choose a CRM JSON export.");
      }
      event.target.value = "";
    };
    reader.readAsText(file);
  });
  load();
  render();
}());
</script>
