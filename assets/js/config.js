// Marv-site runtime config. Safe to commit (no secrets).
// Update these two values after Lee creates the Supabase project:
//   1. LEAD_INTAKE_URL  — https://<project-ref>.functions.supabase.co/lead-intake
//   2. FORM_TOKEN       — value of cops.clients.public_form_token for marv-thorn tenant
//
// Until then, the form will show a friendly "preview mode" message on submit.
window.MARV_CONFIG = {
  LEAD_INTAKE_URL: null,    // e.g. "https://xxxx.functions.supabase.co/lead-intake"
  FORM_TOKEN:      null,    // e.g. "b2f7…"  — tenant's public_form_token
};
