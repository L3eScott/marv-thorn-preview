// Marv-site runtime config. Safe to commit (no secrets).
// LEAD_INTAKE_URL points at the Supabase Edge Function.
// FORM_TOKEN is Marv's tenant public_form_token (public by design — RLS + token
// pairing is what protects, not secrecy of the token itself).
window.MARV_CONFIG = {
  LEAD_INTAKE_URL: "https://ksctixaxseoxuaeynyck.supabase.co/functions/v1/lead-intake",
  FORM_TOKEN:      "5abaa68a-4666-4572-82d1-8b007efd8cc2",
};
