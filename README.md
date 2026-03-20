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
git clone https://github.com/vishnurthn/red-thread
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
[![RED-THREAD Demo Video](https://ibb.co/d0t5QSC8)](https://drive.google.com/file/d/13Fk0a72s53vqCrd3dfpV9RmhuMU19_hD/view?usp=sharing)
*Click the image above to watch the 3-minute project walkthrough.*

## Statistics
RedThread: Closing the 12,000-Death Daily Gap
The Problem:
India faces an annual shortfall of 1.1 million blood units, resulting in over 12,000 preventable deaths daily. The primary cause is not a lack of donors, but a "Communication Lag." Current methods rely on passive social media posts or unfiltered WhatsApp groups that are slow, disorganized, and often reach people too far away to help, leading to "alert fatigue" and fatal delays.

The RedThread Solution:
As Team Leader, I developed a result-oriented system that replaces passive outreach with Instant Triple-Alert Technology. Our platform triggers simultaneous automated calls, WhatsApp, and SMS alerts to verified donors. By using Tiered Radius Escalation (prioritizing donors within 0–5km), we slash response times from hours to minutes.

The Impact:
Applying Full-Stack principles from my internship at Velan Dev Solutions, I led the integration of a gamified rewards dashboard to ensure donor retention. By combining high-speed localized alerts with long-term engagement, RedThread ensures that "lack of time" is never the reason a life is lost.
