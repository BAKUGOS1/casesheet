"""Front-end views.

Every view is presentational: it picks demo content out of ``demo_data`` and
renders a template. There is no persistence, no form handling and no service
call anywhere in this project.
"""

from django.shortcuts import render

from frontend import demo_data

# The kiosk progress rail, shared by every patient-facing screen.
KIOSK_FLOW = [
    {"slug": "identify", "label": "Identify", "url": "identify"},
    {"slug": "consent", "label": "Consent", "url": "consent"},
    {"slug": "complaint", "label": "Complaint", "url": "complaint"},
    {"slug": "interview", "label": "History", "url": "interview"},
    {"slug": "ayush", "label": "Ayurveda", "url": "ayush"},
    {"slug": "documents", "label": "Documents", "url": "documents"},
    {"slug": "summary", "label": "Review", "url": "summary"},
]


def _flow(active):
    """Annotate the kiosk rail with done / current / upcoming state."""
    index = next((i for i, s in enumerate(KIOSK_FLOW) if s["slug"] == active), -1)
    steps = []
    for i, step in enumerate(KIOSK_FLOW):
        steps.append(
            dict(
                step,
                number=i + 1,
                state="done" if i < index else ("current" if i == index else "todo"),
            )
        )
    return {
        "flow": steps,
        "flow_active": active,
        "flow_position": index + 1,
        "flow_total": len(KIOSK_FLOW),
    }


# --- Patient kiosk ----------------------------------------------------------


def welcome(request):
    return render(request, "kiosk/welcome.html")


def identify(request):
    context = _flow("identify")
    context["methods"] = demo_data.IDENTIFY_METHODS
    return render(request, "kiosk/identify.html", context)


def consent(request):
    context = _flow("consent")
    context["consent_items"] = demo_data.CONSENT_ITEMS
    context["patient"] = demo_data.PATIENT
    return render(request, "kiosk/consent.html", context)


def complaint(request):
    context = _flow("complaint")
    context["complaints"] = demo_data.COMPLAINTS
    context["regions"] = demo_data.BODY_REGIONS
    context["selected"] = request.GET.get("picked", "chest-pain")
    return render(request, "kiosk/complaint.html", context)


def interview(request):
    steps = demo_data.INTERVIEW_STEPS
    try:
        number = int(request.GET.get("step", 1))
    except (TypeError, ValueError):
        number = 1
    number = max(1, min(number, len(steps)))

    step = steps[number - 1]
    context = _flow("interview")
    context.update(
        {
            "step": step,
            "step_number": number,
            "step_total": len(steps),
            "progress": int(number * 100 / len(steps)),
            "previous_step": number - 1 if number > 1 else None,
            "next_step": number + 1 if number < len(steps) else None,
            "captured": [s["captured"] for s in steps[: number - 1]],
            "red_flag": step.get("red_flag"),
            "mode": request.GET.get("mode", "voice"),
        }
    )
    return render(request, "kiosk/interview.html", context)


def ayush(request):
    context = _flow("ayush")
    context["parameters"] = demo_data.AYUSH_PARAMETERS
    context["active"] = request.GET.get("p", "prakriti")
    return render(request, "kiosk/ayush.html", context)


def documents(request):
    context = _flow("documents")
    context["documents"] = demo_data.SCANNED_DOCUMENTS
    context["timeline"] = demo_data.DOCUMENT_TIMELINE
    context["extracted_count"] = len([d for d in demo_data.SCANNED_DOCUMENTS if d["status"] == "extracted"])
    return render(request, "kiosk/documents.html", context)


def summary(request):
    context = _flow("summary")
    context["sections"] = demo_data.SUMMARY_SECTIONS
    context["patient"] = demo_data.PATIENT
    return render(request, "kiosk/summary.html", context)


def done(request):
    context = {
        "token": demo_data.TOKEN,
        "patient": demo_data.PATIENT,
    }
    return render(request, "kiosk/done.html", context)


# --- Clinician workspace ----------------------------------------------------


def clinician_queue(request):
    query = request.GET.get("q", "")
    rows = demo_data.QUEUE
    if query:
        needle = query.lower()
        rows = [r for r in rows if needle in r["name"].lower() or needle in r["complaint"].lower() or needle in r["token"].lower()]
    context = {
        "queue": rows,
        "query": query,
        "stats": demo_data.QUEUE_STATS,
        "active_nav": "queue",
    }
    return render(request, "clinician/queue.html", context)


def clinician_patient(request):
    context = {
        "patient": demo_data.PATIENT,
        "sections": demo_data.SUMMARY_SECTIONS,
        "documents": demo_data.SCANNED_DOCUMENTS,
        "timeline": demo_data.DOCUMENT_TIMELINE,
        "vitals": demo_data.VITALS,
        "red_flag": demo_data.INTERVIEW_STEPS[3]["red_flag"],
        "active_nav": "queue",
    }
    return render(request, "clinician/patient.html", context)


# --- Patient portal ---------------------------------------------------------


def portal_login(request):
    return render(request, "patient/login.html", {"active_nav": "login"})


def portal_dashboard(request):
    context = {
        "patient": demo_data.PATIENT,
        "visits": demo_data.PORTAL_VISITS,
        "records": demo_data.PORTAL_RECORDS,
        "medications": demo_data.PORTAL_MEDICATIONS,
        "active_nav": "dashboard",
    }
    return render(request, "patient/dashboard.html", context)


def portal_records(request):
    context = {
        "patient": demo_data.PATIENT,
        "records": demo_data.PORTAL_RECORDS,
        "timeline": demo_data.DOCUMENT_TIMELINE,
        "active_nav": "records",
    }
    return render(request, "patient/records.html", context)


# --- Reviewer index ---------------------------------------------------------


def screens(request):
    return render(request, "screens.html", {"groups": demo_data.SCREEN_GROUPS})
