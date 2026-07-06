// Contact-form handler. Progressive enhancement — the form works without JS
// (falls back to the action URL if we ever set one). With JS, we POST to the
// Supabase Edge Function and show a friendly inline confirmation.

(function () {
  const form = document.querySelector('form.lead');
  if (!form) return;

  const cfg = window.MARV_CONFIG || {};
  const endpoint = cfg.LEAD_INTAKE_URL;
  const token    = cfg.FORM_TOKEN;

  const submitBtn = form.querySelector('button[type="submit"]');
  const note      = form.querySelector('.form-note');

  function setStatus(kind, msg) {
    let el = form.querySelector('.form-status');
    if (!el) {
      el = document.createElement('div');
      el.className = 'form-status';
      el.style.cssText = 'padding:.9rem 1rem;border-radius:.75rem;margin-top:.75rem;font-size:.95rem;line-height:1.45;';
      form.appendChild(el);
    }
    if (kind === 'ok') {
      el.style.background   = '#EAF3ED';
      el.style.border       = '1px solid #7FA891';
      el.style.color        = '#1F3A2E';
    } else if (kind === 'preview') {
      el.style.background   = 'rgba(197,95,63,0.10)';
      el.style.border       = '1px solid #C55F3F';
      el.style.color        = '#7a2c14';
    } else {
      el.style.background   = '#FBEBE7';
      el.style.border       = '1px solid #C55F3F';
      el.style.color        = '#7a2c14';
    }
    el.textContent = msg;
  }

  form.addEventListener('submit', async (e) => {
    // If endpoint isn't configured, we're in preview — don't lose the visitor.
    if (!endpoint || !token) {
      e.preventDefault();
      setStatus('preview', 'Preview mode: the form is wired but not yet connected to Marv\'s live inbox. Once configured, submissions will land in Marv\'s CRM immediately.');
      return;
    }
    e.preventDefault();
    submitBtn.disabled = true;
    submitBtn.textContent = 'Sending…';
    setStatus('ok', ''); // clear
    try {
      const data = new FormData(form);
      const body = {
        first_name:        (data.get('name') || '').toString(),
        email:             (data.get('email') || '').toString(),
        phone:             (data.get('phone') || '').toString(),
        postal_code:       (data.get('zip') || '').toString(),
        coverage_interest: (data.get('line') || '').toString(),
        message:           (data.get('message') || '').toString(),
        source_detail:     'marv-thorn-preview/contact',
      };
      const res = await fetch(endpoint, {
        method: 'POST',
        headers: { 'content-type': 'application/json', 'x-form-token': token },
        body: JSON.stringify(body),
      });
      if (res.ok) {
        setStatus('ok', 'Got it — Marv will follow up within one business day. If it\'s urgent, call (713) 555-0142.');
        form.reset();
      } else {
        const j = await res.json().catch(() => ({}));
        setStatus('err', 'We couldn\'t submit that — please try again or call (713) 555-0142. (' + (j.error || res.status) + ')');
      }
    } catch (err) {
      setStatus('err', 'Network error — please try again or call (713) 555-0142.');
    } finally {
      submitBtn.disabled = false;
      submitBtn.textContent = 'Send to Marv';
    }
  });
})();
