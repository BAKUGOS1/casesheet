"""Static demo content for the CaseSheet front-end prototype.

Nothing here touches a database or a model. Every screen imports from this
module so the interface can be demonstrated with realistic content.
English only, and deliberately short: a kiosk screen should hold one idea.
"""

# --- Step 1: identify -------------------------------------------------------

IDENTIFY_METHODS = [
    {"slug": "abha", "icon": "id-card", "title": "Scan ABHA card", "subtitle": "Hold the card under the scanner"},
    {"slug": "abha-number", "icon": "keypad", "title": "Type ABHA number", "subtitle": "14 digits, or your ABHA address"},
    {"slug": "aadhaar", "icon": "fingerprint", "title": "Aadhaar fingerprint", "subtitle": "Place your thumb on the reader"},
    {"slug": "new", "icon": "user-plus", "title": "I am new here", "subtitle": "Register in under a minute"},
]

# --- Step 2: consent --------------------------------------------------------

CONSENT_ITEMS = [
    {
        "slug": "capture",
        "title": "Record my history here",
        "plain": "Save my answers for the doctor I am about to meet.",
        "required": True,
        "default_on": True,
    },
    {
        "slug": "documents",
        "title": "Scan my papers",
        "plain": "Read my old prescriptions and reports into my file.",
        "required": False,
        "default_on": True,
    },
    {
        "slug": "abha-link",
        "title": "Save to my ABHA record",
        "plain": "Keep this visit in my national health record.",
        "required": False,
        "default_on": True,
    },
    {
        "slug": "past-records",
        "title": "Show my past records",
        "plain": "Let today's doctor open reports from earlier visits.",
        "required": False,
        "default_on": False,
    },
]

# --- Step 3: chief complaint ------------------------------------------------

COMPLAINTS = [
    {"slug": "fever", "icon": "thermometer", "label": "Fever"},
    {"slug": "chest-pain", "icon": "heart", "label": "Chest pain"},
    {"slug": "cough", "icon": "cough", "label": "Cough"},
    {"slug": "headache", "icon": "head", "label": "Headache"},
    {"slug": "stomach", "icon": "stomach", "label": "Stomach pain"},
    {"slug": "joint", "icon": "joint", "label": "Joint or back pain"},
    {"slug": "weakness", "icon": "weakness", "label": "Weakness"},
    {"slug": "other", "icon": "dots", "label": "Something else"},
]

# Touch targets on the body map, in the coordinates of its 320x250 viewBox.
BODY_REGIONS = [
    {"slug": "head", "label": "Head", "cx": 160, "cy": 35},
    {"slug": "chest", "label": "Chest", "cx": 160, "cy": 95},
    {"slug": "stomach", "label": "Stomach", "cx": 160, "cy": 137},
    {"slug": "left-arm", "label": "Arm", "cx": 104, "cy": 127},
    {"slug": "right-arm", "label": "Arm", "cx": 216, "cy": 127},
    {"slug": "left-leg", "label": "Leg", "cx": 139, "cy": 209},
    {"slug": "right-leg", "label": "Leg", "cx": 181, "cy": 209},
]

# --- Step 4: the conversational interview ----------------------------------
# Each step mirrors the SOCRATES probing described in the problem statement.

INTERVIEW_STEPS = [
    {
        "number": 1,
        "probe": "Site",
        "question": "Where exactly is the pain?",
        "kind": "options",
        "options": [
            {"slug": "centre", "label": "Middle of the chest", "icon": "heart"},
            {"slug": "left", "label": "Left side", "icon": "arrow-left"},
            {"slug": "right", "label": "Right side", "icon": "arrow-right"},
            {"slug": "spread", "label": "All over", "icon": "dots"},
        ],
        "transcript": [
            {"who": "kiosk", "text": "You told me you have chest pain. Where exactly is it?"},
            {"who": "patient", "text": "In the middle, when I walk fast."},
        ],
        "captured": "Central chest",
    },
    {
        "number": 2,
        "probe": "Onset",
        "question": "When did it start?",
        "kind": "options",
        "options": [
            {"slug": "today", "label": "Today", "icon": "clock"},
            {"slug": "days", "label": "A few days", "icon": "calendar"},
            {"slug": "weeks", "label": "2 to 4 weeks", "icon": "calendar"},
            {"slug": "months", "label": "Months or longer", "icon": "calendar"},
        ],
        "transcript": [
            {"who": "kiosk", "text": "When did the pain start?"},
            {"who": "patient", "text": "Three weeks ago. It comes when I climb stairs."},
        ],
        "captured": "3 weeks, on exertion",
    },
    {
        "number": 3,
        "probe": "Severity",
        "question": "How bad is it?",
        "kind": "scale",
        "scale": [
            {"value": 2, "label": "Mild", "face": "sev-1"},
            {"value": 4, "label": "Uncomfortable", "face": "sev-2"},
            {"value": 6, "label": "Bad", "face": "sev-3"},
            {"value": 8, "label": "Very bad", "face": "sev-4"},
            {"value": 10, "label": "Worst ever", "face": "sev-5"},
        ],
        "transcript": [
            {"who": "kiosk", "text": "How bad is it when it comes?"},
            {"who": "patient", "text": "Like pressure. Seven out of ten."},
        ],
        "captured": "Pressure-like, 7 of 10",
    },
    {
        "number": 4,
        "probe": "Radiation",
        "question": "Does the pain travel anywhere else?",
        "kind": "options",
        "options": [
            {"slug": "arm", "label": "Left arm", "icon": "arrow-left"},
            {"slug": "jaw", "label": "Jaw or neck", "icon": "head"},
            {"slug": "back", "label": "Back", "icon": "joint"},
            {"slug": "none", "label": "No", "icon": "check"},
        ],
        "transcript": [
            {"who": "kiosk", "text": "Does the pain travel anywhere else?"},
            {"who": "patient", "text": "Down the left arm. And I sweat with it."},
        ],
        "captured": "Left arm, with sweating",
        "red_flag": {
            "title": "Possible cardiac emergency",
            "detail": "Triage staff alerted. This patient moves ahead of the queue.",
        },
    },
    {
        "number": 5,
        "probe": "Past illness",
        "question": "Do you take medicine for any of these?",
        "kind": "multi",
        "options": [
            {"slug": "bp", "label": "Blood pressure", "icon": "activity"},
            {"slug": "sugar", "label": "Diabetes", "icon": "pill"},
            {"slug": "thyroid", "label": "Thyroid", "icon": "pill"},
            {"slug": "asthma", "label": "Asthma", "icon": "cough"},
            {"slug": "heart", "label": "Heart problem", "icon": "heart"},
            {"slug": "none", "label": "None", "icon": "check"},
        ],
        "transcript": [
            {"who": "kiosk", "text": "Do you take medicine for blood pressure or sugar?"},
            {"who": "patient", "text": "Blood pressure, six years. Telma 40."},
        ],
        "captured": "Hypertension, 6 years",
    },
    {
        "number": 6,
        "probe": "Allergy",
        "question": "Has any medicine ever given you a rash or swelling?",
        "kind": "options",
        "options": [
            {"slug": "medicine", "label": "Yes, a medicine", "icon": "pill"},
            {"slug": "food", "label": "Yes, a food", "icon": "stomach"},
            {"slug": "unsure", "label": "Not sure", "icon": "dots"},
            {"slug": "none", "label": "No", "icon": "check"},
        ],
        "transcript": [
            {"who": "kiosk", "text": "Has any medicine ever given you a rash?"},
            {"who": "patient", "text": "A sulpha tablet. Rash all over."},
        ],
        "captured": "Sulphonamides, rash",
    },
]

# --- Step 5: AYUSH / Dashavidha Pariksha -----------------------------------

AYUSH_PARAMETERS = [
    {
        "slug": "prakriti",
        "name": "Prakriti",
        "gloss": "Constitution",
        "question": "How is your body most of the time?",
        "options": ["Thin and quick", "Warm, sharp appetite", "Steady and heavy"],
        "answer": "Pitta-Kapha",
    },
    {
        "slug": "vikriti",
        "name": "Vikriti",
        "gloss": "Current imbalance",
        "question": "What feels different from usual?",
        "options": ["Restless", "Burning, acidity", "Heavy, sluggish"],
        "answer": "Pitta vriddhi",
    },
    {
        "slug": "agni",
        "name": "Agni",
        "gloss": "Digestion",
        "question": "How is your appetite?",
        "options": ["Irregular", "Very strong", "Weak", "Balanced"],
        "answer": "Tikshna",
    },
    {
        "slug": "koshtha",
        "name": "Koshtha",
        "gloss": "Bowel",
        "question": "How are your motions?",
        "options": ["Hard", "Regular", "Loose"],
        "answer": "Madhyama",
    },
    {
        "slug": "sara",
        "name": "Sara",
        "gloss": "Tissue quality",
        "question": "How is your stamina?",
        "options": ["Tires quickly", "Average", "Strong all day"],
        "answer": "Madhyama",
    },
    {
        "slug": "samhanana",
        "name": "Samhanana",
        "gloss": "Build",
        "question": "How would you describe your build?",
        "options": ["Lean", "Medium", "Heavy"],
        "answer": "Madhyama",
    },
    {
        "slug": "pramana",
        "name": "Pramana",
        "gloss": "Measurements",
        "question": "Measured at the kiosk",
        "options": ["168 cm", "74 kg", "BMI 26.2"],
        "answer": "BMI 26.2",
    },
    {
        "slug": "satmya",
        "name": "Satmya",
        "gloss": "What suits you",
        "question": "What food suits you best?",
        "options": ["Warm food", "Cool food", "Mixed"],
        "answer": "Mixed",
    },
    {
        "slug": "sattva",
        "name": "Sattva",
        "gloss": "Mental strength",
        "question": "How do you handle stress?",
        "options": ["Anxious quickly", "Manage most days", "Stay calm"],
        "answer": "Madhyama",
    },
    {
        "slug": "vaya",
        "name": "Vaya",
        "gloss": "Age group",
        "question": "Taken from your record",
        "options": ["Bala", "Madhya", "Vriddha"],
        "answer": "Madhya",
    },
]

# --- Step 6: documents ------------------------------------------------------

SCANNED_DOCUMENTS = [
    {
        "slug": "presc-2026-06",
        "kind": "Prescription",
        "icon": "file-text",
        "title": "OPD prescription",
        "source": "City General Hospital",
        "date": "14 Jun 2026",
        "status": "extracted",
        "confidence": 96,
        "handwritten": True,
        "extracted": [
            {"label": "Telmisartan", "value": "40 mg daily"},
            {"label": "Aspirin", "value": "75 mg daily"},
        ],
    },
    {
        "slug": "lipid-2026-06",
        "kind": "Lab report",
        "icon": "activity",
        "title": "Lipid profile",
        "source": "Sunrise Diagnostics",
        "date": "12 Jun 2026",
        "status": "extracted",
        "confidence": 99,
        "handwritten": False,
        "extracted": [
            {"label": "Cholesterol", "value": "244", "abnormal": True, "range": "< 200"},
            {"label": "LDL", "value": "168", "abnormal": True, "range": "< 100"},
            {"label": "HDL", "value": "38", "abnormal": True, "range": "> 40"},
        ],
    },
    {
        "slug": "discharge-2024",
        "kind": "Discharge summary",
        "icon": "file-text",
        "title": "Discharge summary",
        "source": "District Hospital",
        "date": "03 Sep 2024",
        "status": "extracted",
        "confidence": 91,
        "handwritten": False,
        "extracted": [
            {"label": "Diagnosis", "value": "Dengue fever"},
        ],
    },
    {
        "slug": "ecg-2026-06",
        "kind": "Investigation",
        "icon": "activity",
        "title": "ECG strip",
        "source": "Captured here",
        "date": "Today",
        "status": "reading",
        "confidence": 0,
        "handwritten": False,
        "extracted": [],
    },
]

DOCUMENT_TIMELINE = [
    {"date": "Sep 2024", "label": "Dengue admission"},
    {"date": "Jun 2026", "label": "Hypertension review"},
    {"date": "Jun 2026", "label": "Lipid profile", "abnormal": True},
    {"date": "Today", "label": "This visit", "current": True},
]

# --- Step 7: the generated summary -----------------------------------------

SUMMARY_SECTIONS = [
    {
        "slug": "chief-complaint",
        "title": "Chief complaint",
        "confidence": "high",
        "lines": [
            "Central chest pain on exertion, 3 weeks",
            "Radiates to the left arm, with sweating",
        ],
        "source": "Spoken",
    },
    {
        "slug": "hpi",
        "title": "History of present illness",
        "confidence": "high",
        "lines": [
            "Gradual onset, pressure-like, 7 of 10 at worst",
            "Brought on by stairs, eases with rest in 5 minutes",
            "No syncope, palpitations or breathlessness at rest",
        ],
        "source": "Spoken",
    },
    {
        "slug": "past-history",
        "title": "Past medical history",
        "confidence": "high",
        "lines": [
            "Hypertension, 6 years, on treatment",
            "Dengue fever, Sep 2024, recovered",
            "No surgery",
        ],
        "source": "Spoken and discharge summary",
    },
    {
        "slug": "drugs",
        "title": "Medicines and allergy",
        "confidence": "high",
        "lines": [
            "Telmisartan 40 mg daily",
            "Aspirin 75 mg daily",
            "Allergy: sulphonamides, rash",
        ],
        "source": "Scanned prescription",
        "alert": "Allergy",
    },
    {
        "slug": "family",
        "title": "Family history",
        "confidence": "medium",
        "lines": [
            "Father, heart attack at 58",
            "Mother, diabetes",
        ],
        "source": "Spoken",
    },
    {
        "slug": "personal",
        "title": "Personal history",
        "confidence": "medium",
        "lines": [
            "Chewing tobacco, 8 years, 3 to 4 a day",
            "Sedentary work, late dinner, sleep 5 to 6 hours",
        ],
        "source": "Spoken",
    },
    {
        "slug": "ros",
        "title": "Review of systems",
        "confidence": "medium",
        "lines": [
            "Heart: chest pain on exertion, no swelling",
            "Chest: no cough, no breathlessness at rest",
            "Stomach: acidity most evenings",
        ],
        "source": "Tapped answers",
    },
    {
        "slug": "ayush",
        "title": "Dashavidha Pariksha",
        "confidence": "medium",
        "lines": [
            "Prakriti Pitta-Kapha, Vikriti Pitta vriddhi",
            "Agni Tikshna, Koshtha Madhyama",
        ],
        "source": "Ayurvedic assessment",
    },
    {
        "slug": "investigations",
        "title": "Past investigations",
        "confidence": "high",
        "lines": [
            "Lipid profile, 12 Jun 2026: cholesterol 244, LDL 168",
            "ECG photo, today, awaiting review",
        ],
        "source": "Scanned reports",
        "alert": "3 out of range",
    },
]

# --- Token / triage ---------------------------------------------------------

TOKEN = {
    "number": "A-042",
    "department": "General Medicine OPD",
    "room": "Room 12, ground floor",
    "priority": True,
    "priority_reason": "Chest pain with radiation",
    "wait": "Called next",
    "abha": "12-3456-7890-1234",
}

# --- Clinician queue --------------------------------------------------------

QUEUE = [
    {
        "token": "A-042",
        "name": "Ramesh Kumar",
        "age": 52,
        "sex": "M",
        "complaint": "Chest pain on exertion, 3 weeks",
        "waited": "4 min",
        "status": "Ready",
        "priority": "red",
        "flag": "Possible cardiac",
        "docs": 4,
        "ayush": True,
    },
    {
        "token": "A-039",
        "name": "Sunita Devi",
        "age": 34,
        "sex": "F",
        "complaint": "Fever with rash, 4 days",
        "waited": "18 min",
        "status": "Ready",
        "priority": "amber",
        "flag": "Platelets falling",
        "docs": 2,
        "ayush": False,
    },
    {
        "token": "A-040",
        "name": "Abdul Rahman",
        "age": 67,
        "sex": "M",
        "complaint": "Knee pain, 6 months",
        "waited": "16 min",
        "status": "Ready",
        "priority": "none",
        "flag": "",
        "docs": 3,
        "ayush": True,
    },
    {
        "token": "A-041",
        "name": "Lakshmi Narayanan",
        "age": 45,
        "sex": "F",
        "complaint": "Acidity, weight loss, 2 months",
        "waited": "11 min",
        "status": "Ready",
        "priority": "amber",
        "flag": "Weight loss",
        "docs": 1,
        "ayush": True,
    },
    {
        "token": "A-043",
        "name": "Mohan Prasad",
        "age": 29,
        "sex": "M",
        "complaint": "Cough, 3 weeks",
        "waited": "6 min",
        "status": "In interview",
        "priority": "none",
        "flag": "",
        "docs": 0,
        "ayush": False,
    },
    {
        "token": "A-044",
        "name": "Geeta Sharma",
        "age": 58,
        "sex": "F",
        "complaint": "Follow-up, diabetes",
        "waited": "2 min",
        "status": "Scanning",
        "priority": "none",
        "flag": "",
        "docs": 5,
        "ayush": True,
    },
]

QUEUE_STATS = [
    {"label": "Waiting", "value": "18"},
    {"label": "Histories ready", "value": "6"},
    {"label": "Red flags", "value": "1"},
    {"label": "Minutes saved each", "value": "6.4"},
]

VITALS = [
    {"label": "BP", "value": "148/94", "abnormal": True},
    {"label": "Pulse", "value": "92", "abnormal": False},
    {"label": "SpO2", "value": "97", "abnormal": False},
    {"label": "Temp", "value": "98.4", "abnormal": False},
    {"label": "BMI", "value": "26.2", "abnormal": True},
]

# --- Patient portal ---------------------------------------------------------

PORTAL_VISITS = [
    {
        "date": "10 Sep 2026",
        "place": "All India Institute of Ayurveda",
        "doctor": "Dr. A. Sharma",
        "summary": "Chest pain on exertion, ECG advised",
        "current": True,
    },
    {
        "date": "14 Jun 2026",
        "place": "City General Hospital",
        "doctor": "Dr. R. Menon",
        "summary": "Hypertension review",
        "current": False,
    },
    {
        "date": "03 Sep 2024",
        "place": "District Hospital",
        "doctor": "Dr. P. Iyer",
        "summary": "Dengue fever, 4 days admitted",
        "current": False,
    },
]

PORTAL_RECORDS = [
    {"title": "History summary", "date": "10 Sep 2026", "kind": "Summary"},
    {"title": "ECG strip", "date": "10 Sep 2026", "kind": "Investigation"},
    {"title": "Lipid profile", "date": "12 Jun 2026", "kind": "Lab report", "abnormal": True},
    {"title": "OPD prescription", "date": "14 Jun 2026", "kind": "Prescription"},
    {"title": "Discharge summary", "date": "03 Sep 2024", "kind": "Discharge"},
]

PORTAL_MEDICATIONS = [
    {"name": "Telmisartan 40 mg", "freq": "Once daily, morning"},
    {"name": "Aspirin 75 mg", "freq": "Once daily, after food"},
]

PATIENT = {
    "name": "Ramesh Kumar",
    "age": 52,
    "sex": "Male",
    "abha": "12-3456-7890-1234",
    "token": "A-042",
}

# --- Screen gallery ---------------------------------------------------------

SCREEN_GROUPS = [
    {
        "title": "Patient kiosk",
        "screens": [
            {"url": "welcome", "name": "Welcome", "desc": "Start screen and accessibility controls."},
            {"url": "identify", "name": "Identify", "desc": "ABHA, Aadhaar or new registration."},
            {"url": "consent", "name": "Consent", "desc": "Four choices, each revocable."},
            {"url": "complaint", "name": "Chief complaint", "desc": "Body map and picture grid."},
            {"url": "interview", "name": "Interview", "desc": "Speak or tap, six questions."},
            {"url": "ayush", "name": "Dashavidha Pariksha", "desc": "Ten-fold Ayurvedic assessment."},
            {"url": "documents", "name": "Scan documents", "desc": "Capture and read old papers."},
            {"url": "summary", "name": "Review", "desc": "Patient confirms before sending."},
            {"url": "done", "name": "Token", "desc": "Token, room and priority."},
        ],
    },
    {
        "title": "Clinician workspace",
        "screens": [
            {"url": "clinician_queue", "name": "OPD queue", "desc": "Red flags first, not arrival order."},
            {"url": "clinician_patient", "name": "History summary", "desc": "Accept, amend or reject the draft."},
        ],
    },
    {
        "title": "Patient portal",
        "screens": [
            {"url": "portal_login", "name": "Login", "desc": "ABHA address and OTP."},
            {"url": "portal_dashboard", "name": "My record", "desc": "Visits, medicines, documents."},
            {"url": "portal_records", "name": "My documents", "desc": "Everything digitised here."},
        ],
    },
]
