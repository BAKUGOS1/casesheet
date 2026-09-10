from django.urls import path

from frontend import views

urlpatterns = [
    # Patient kiosk flow
    path("", views.welcome, name="welcome"),
    path("identify/", views.identify, name="identify"),
    path("consent/", views.consent, name="consent"),
    path("complaint/", views.complaint, name="complaint"),
    path("interview/", views.interview, name="interview"),
    path("ayush/", views.ayush, name="ayush"),
    path("documents/", views.documents, name="documents"),
    path("summary/", views.summary, name="summary"),
    path("done/", views.done, name="done"),
    # Clinician workspace
    path("clinician/", views.clinician_queue, name="clinician_queue"),
    path("clinician/patient/", views.clinician_patient, name="clinician_patient"),
    # Patient portal
    path("portal/login/", views.portal_login, name="portal_login"),
    path("portal/", views.portal_dashboard, name="portal_dashboard"),
    path("portal/records/", views.portal_records, name="portal_records"),
    # Reviewer index of every screen
    path("screens/", views.screens, name="screens"),
]
