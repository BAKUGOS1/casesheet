# CaseSheet — front end for SIH26047 (Patient Case-Taking Software)

A UI-only Django project for the problem statement *Patient Case-Taking Software*
(All India Institute of Ayurveda, Ministry of Ayush). A "case sheet" is what the
patient record is called in an Indian hospital, and case-taking is what this software does.

**Django and nothing else.** Django templates, Django static files, hand-written CSS
and a little plain browser JavaScript. No React, no Tailwind, no Bootstrap, no CDN,
no build step, no Node. No models, no database, no external services — every screen
renders from fixed demo content in `frontend/demo_data.py`. English only.

## Run it

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
```

Then open <http://127.0.0.1:8000/screens/> for an index of every screen.

There is no database, so `migrate` is neither needed nor possible: `DATABASES` is empty
and `INSTALLED_APPS` holds only `django.contrib.staticfiles` and this project's `frontend` app.

## Screens

| URL | Screen |
| --- | --- |
| `/` | Welcome |
| `/identify/` | ABHA scan, ABHA number, Aadhaar fingerprint, or new registration |
| `/consent/` | Four consent choices, each revocable |
| `/complaint/` | Body map with labelled regions, plus a picture grid |
| `/interview/?step=1..6` | The interview, in speak or tap mode |
| `/ayush/` | Dashavidha Pariksha |
| `/documents/` | Scanning, extraction and the medical timeline |
| `/summary/` | The structured history the patient confirms |
| `/done/` | Token, room and priority |
| `/clinician/` | OPD queue with red-flag escalation |
| `/clinician/patient/` | The history summary a physician accepts or amends |
| `/portal/login/` | Patient portal login |
| `/portal/` | Patient dashboard |
| `/portal/records/` | Patient documents |
| `/screens/` | Index of every screen |

## How the problem statement maps onto the UI

- **Module A, conversational multimodal history** — `/interview/`. Every question can be
  spoken or tapped (`Speak` / `Tap`). Each carries the SOCRATES probe it belongs to.
  Step 4 fires the red-flag path.
- **Module B, document digitisation** — `/documents/`. Scanner view, per-document extraction
  with a confidence figure, out-of-range lab values highlighted, auto-ordered timeline.
- **Module C, structured summary** — `/summary/` for the patient, `/clinician/patient/` for
  the physician, in the standard clinical order. The physician view is an editable draft
  with accept / amend / reject, never a diagnosis.
- **Module D, consent, privacy and ABDM** — `/consent/`, plus the ABHA identity and consent
  panels that recur across the flow.
- **AYUSH history mode** — `/ayush/`: all ten Dashavidha Pariksha parameters.
- **Accessibility** — the header of every kiosk screen: three text sizes, high contrast,
  audio-guide toggle, call a helper. Preferences persist in `localStorage`.

## Writing rules used here

One idea per screen, one line per idea. Headings are questions the patient would ask
themselves. No paragraph of explanation where a label will do, and nothing repeated on
two screens. If a screen has to teach the patient something, it is doing too much.

## Layout

```
casesheet/
  manage.py
  casesheet/            project settings, urls, wsgi, asgi
  frontend/             app: urls, views, demo_data, context_processors
  templates/
    base.html           document shell
    screens.html        reviewer index
    partials/           icon sprite, accessibility bar, progress rail
    kiosk/              patient-facing screens
    clinician/          clinician workspace
    patient/            patient portal
  static/
    css/base.css        design tokens, reset, shared components
    css/kiosk.css       kiosk surface
    css/clinician.css   clinician workspace and patient portal
    js/a11y.js          text size, contrast, audio
    js/kiosk.js         selection states, consent switches, microphone
```

## Notes for whoever wires up the back end

- Views take no POST and hold no state. Each builds a context dict and renders.
- All display content lives in `frontend/demo_data.py`; swapping it for real querysets
  should not require template changes beyond field names.
- The interview advances through `?step=`, so server-driven adaptive branching drops in
  without touching the front end.
- The kiosk is English-only by design for now. Nothing is hard-coded against English:
  the strings live in templates, so `{% trans %}` and Django's i18n machinery can be
  layered on when the other languages are added.
