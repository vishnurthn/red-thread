## 🩸 RED-THREAD: Smart Emergency Blood Synchronization
RED-THREAD is a full-stack emergency response system designed to minimize the "Critical Time" delay. It connects hospitals with eligible donors in real-time using location-based geocoding and automated search expansion.

## 🌟 Key Innovations
Dual-Portal Ecosystem: Separate, synchronized interfaces for Medical Administrators and Donors.

Automated Escalation Logic: 

Phase 1: Instant alert to donors within 5km.

Phase 2: If no response is received within 5 minutes, the search radius automatically expands to 10km to ensure patient safety.

Note: While the prototype was demonstrated with a 30-second timer for speed, the production logic is set to a 5-minute window to allow for human response time.

Pincode-to-Coordinate Mapping: Uses Geopy and Nominatim to convert donor pincodes into live geographic coordinates for precise distance sorting.

Medical Eligibility Filter: Integrated logic to disqualify donors based on health criteria (e.g., recent tattoos), ensuring medical compliance.

Live Navigation: One-click redirection to a Leaflet.js map showing the donor the exact route to the hospital.


## 🛠️ Tech Stack

Backend: Python (Flask), Flask-CORS, Geopy.

Frontend: HTML5, CSS3 (Glassmorphism UI), JavaScript (ES6+).

Mapping: Leaflet.js API.

Hardware Integration: C++ (Storage monitoring simulation).

## 📂 Project Structure
```
e-BloodBank/
├── backend/
│   ├── app.py              # Main Flask Server & API Logic
├── frontend/
│   ├── hospital_reg.html   # Admin Onboarding
│   ├── index.html          # Hospital SOS Dashboard
│   ├── register.html       # Donor Registration & Eligibility
│   ├── dashboard.html      # Donor Personal Portal
│   ├── map.html            # Real-time Navigation
│   └── style.css           # Global Aesthetic Styling
└── README.md
```

## 🚀 Getting Started

Clone the repository:
```
Bash
git clone https://github.com/vishnurthn/e-BloodBank.git
```

Initialize the Backend:
```
Bash
cd backend
pip install -r requirements.txt
python app.py
```

Run the Demo:

Open hospital_reg.html to register a facility.

Open register.html in a separate window to join as a donor.

Trigger the SOS from the hospital dashboard and watch the live alert appear on the donor portal.

## 📺 Project Demo
[![RED-THREAD Demo Video](https://ibb.co/d0t5QSC8)](https://youtu.be/o0haNG5YseM)
*Click the image above to watch the 3-minute project walkthrough.*
