from flask import Flask, request, jsonify
from flask_cors import CORS
from geopy.distance import geodesic

app = Flask(__name__)

# CRITICAL FIX: This allows your local HTML file to talk to this Python server
# It solves the "Response to preflight request doesn't pass access control check" error
CORS(app, resources={r"/*": {"origins": "*"}})

# Dataset: 50 Donors with diverse blood groups and distances
donors = [
    # --- NEARBY (0km - 5km) ---
    {"id": 1, "name": "Arjun", "blood_group": "O+", "lat": 13.0285, "lon": 80.0450},
    {"id": 2, "name": "Vishnu", "blood_group": "O+", "lat": 13.0290, "lon": 80.0460},
    {"id": 3, "name": "Priya", "blood_group": "B-", "lat": 13.0300, "lon": 80.0500},
    {"id": 4, "name": "Ananya", "blood_group": "A+", "lat": 13.0270, "lon": 80.0420},
    {"id": 5, "name": "Siddharth", "blood_group": "AB+", "lat": 13.0310, "lon": 80.0480},
    {"id": 6, "name": "Meera", "blood_group": "O-", "lat": 13.0250, "lon": 80.0400},
    {"id": 7, "name": "Karthik", "blood_group": "B+", "lat": 13.0350, "lon": 80.0600},
    {"id": 8, "name": "Tanvi", "blood_group": "A-", "lat": 13.0200, "lon": 80.0300},
    {"id": 9, "name": "Aditya", "blood_group": "AB-", "lat": 13.0400, "lon": 80.0550},
    {"id": 10, "name": "Ishani", "blood_group": "O+", "lat": 13.0282, "lon": 80.0445},

    # --- MID-RANGE (5km - 15km: Porur, Poonamallee, Valasaravakkam) ---
    {"id": 11, "name": "Vikram", "blood_group": "AB+", "lat": 13.0450, "lon": 80.1100},
    {"id": 12, "name": "Sana", "blood_group": "O-", "lat": 13.0520, "lon": 80.1500},
    {"id": 13, "name": "Rohan", "blood_group": "A+", "lat": 13.0100, "lon": 80.1200},
    {"id": 14, "name": "Deepa", "blood_group": "B+", "lat": 13.0600, "lon": 80.1300},
    {"id": 15, "name": "Aravind", "blood_group": "O+", "lat": 12.9900, "lon": 80.0800},
    {"id": 16, "name": "Kavya", "blood_group": "A-", "lat": 13.0700, "lon": 80.1400},
    {"id": 17, "name": "Manoj", "blood_group": "B-", "lat": 13.0300, "lon": 80.1800},
    {"id": 18, "name": "Riya", "blood_group": "AB-", "lat": 13.0900, "lon": 80.1100},
    {"id": 19, "name": "Suresh", "blood_group": "O-", "lat": 13.0000, "lon": 80.1600},
    {"id": 20, "name": "Varun", "blood_group": "A+", "lat": 13.0200, "lon": 80.1900},

    # --- CITY CENTER (15km - 30km: T-Nagar, Central, Adyar) ---
    {"id": 21, "name": "Rahul", "blood_group": "O+", "lat": 13.1000, "lon": 80.1500},
    {"id": 22, "name": "Deepak", "blood_group": "AB-", "lat": 13.0827, "lon": 80.2707},
    {"id": 23, "name": "Sneha", "blood_group": "A+", "lat": 12.9229, "lon": 80.1275},
    {"id": 24, "name": "Rajesh", "blood_group": "B+", "lat": 13.1500, "lon": 80.2000},
    {"id": 25, "name": "Divya", "blood_group": "O-", "lat": 13.0400, "lon": 80.2400},
    {"id": 26, "name": "Amit", "blood_group": "A-", "lat": 13.0600, "lon": 80.2300},
    {"id": 27, "name": "Pooja", "blood_group": "AB+", "lat": 13.0000, "lon": 80.2500},
    {"id": 28, "name": "Naveen", "blood_group": "B-", "lat": 12.9800, "lon": 80.2200},
    {"id": 29, "name": "Swati", "blood_group": "O+", "lat": 13.1200, "lon": 80.2100},
    {"id": 30, "name": "Gaurav", "blood_group": "A+", "lat": 13.0100, "lon": 80.2800},

    # --- PERIPHERY/OUTSKIRTS (30km - 60km: Kanchipuram, Chengalpattu) ---
    {"id": 31, "name": "Abhishek", "blood_group": "B+", "lat": 12.8300, "lon": 79.7000},
    {"id": 32, "name": "Lata", "blood_group": "O-", "lat": 12.6800, "lon": 79.9800},
    {"id": 33, "name": "Vijay", "blood_group": "A+", "lat": 12.9000, "lon": 80.0000},
    {"id": 34, "name": "Preeti", "blood_group": "AB-", "lat": 13.2500, "lon": 80.3000},
    {"id": 35, "name": "Harish", "blood_group": "O+", "lat": 13.3500, "lon": 80.1000},
    {"id": 36, "name": "Anjali", "blood_group": "B-", "lat": 12.7500, "lon": 80.2000},
    {"id": 37, "name": "Sanjay", "blood_group": "A-", "lat": 12.8500, "lon": 80.1500},
    {"id": 38, "name": "Nehal", "blood_group": "AB+", "lat": 13.1800, "lon": 79.9000},
    {"id": 39, "name": "Yash", "blood_group": "O-", "lat": 13.0500, "lon": 79.8000},
    {"id": 40, "name": "Kriti", "blood_group": "B+", "lat": 12.9500, "lon": 80.3500},

    # --- EXTRA VARIED ENTRIES ---
    {"id": 41, "name": "Sameer", "blood_group": "O+", "lat": 13.0289, "lon": 80.0442},
    {"id": 42, "name": "Radhika", "blood_group": "A+", "lat": 13.0320, "lon": 80.0520},
    {"id": 43, "name": "Pranav", "blood_group": "B+", "lat": 13.0410, "lon": 80.0590},
    {"id": 44, "name": "Tara", "blood_group": "O-", "lat": 13.0210, "lon": 80.0320},
    {"id": 45, "name": "Omkar", "blood_group": "AB+", "lat": 13.0380, "lon": 80.0490},
    {"id": 46, "name": "Zoya", "blood_group": "A-", "lat": 13.0550, "lon": 80.1200},
    {"id": 47, "name": "Aryan", "blood_group": "B-", "lat": 13.0780, "lon": 80.1900},
    {"id": 48, "name": "Shruti", "blood_group": "O+", "lat": 13.1100, "lon": 80.2500},
    {"id": 49, "name": "Tushar", "blood_group": "AB-", "lat": 12.9500, "lon": 80.1000},
    {"id": 50, "name": "Ishita", "blood_group": "A+", "lat": 13.0265, "lon": 80.0435}
]

@app.route('/request-blood', methods=['POST'])
def request_blood():
    try:
        data = request.json
        # Coordinates for Saveetha Engineering College area
        h_lat = data.get('lat', 13.0280)
        h_lon = data.get('lon', 80.0440)
        requested_bg = data.get('blood_group')

        print(f"!!! Emergency Request Received: {requested_bg} !!!")

        # 1. Filter by Blood Group and calculate distances
        matches = []
        for d in donors:
            if d['blood_group'] == requested_bg:
                dist = geodesic((h_lat, h_lon), (d['lat'], d['lon'])).km
                matches.append({
                    "id": d['id'],
                    "name": d['name'],
                    "distance_km": round(dist, 2)
                })

        # 2. Logic: Phase 1 (Immediate - within 2km)
        immediate_donors = [d for d in matches if d['distance_km'] <= 2.0]
        
        # 3. Logic: Phase 2 (Escalation - within 10km)
        # These are sent back so the frontend can display them after 10 mins
        escalation_donors = [d for d in matches if 2.0 < d['distance_km'] <= 10.0]

        return jsonify({
            "status": "SOS_ACTIVE",
            "timer_limit_minutes": 10,
            "immediate_donors": immediate_donors,
            "escalation_donors": escalation_donors,
            "total_matches": len(matches)
        }), 200

    except Exception as e:
        print(f"Backend Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Running on 0.0.0.0 makes it accessible across your local network
    app.run(debug=True, host='0.0.0.0', port=5000)

    @app.route('/request-blood', methods=['POST'])
    def request_blood():
        try:
            data = request.json
            h_lat, h_lon = data.get('lat', 13.0280), data.get('lon', 80.0440)
            requested_bg = data.get('blood_group')

            # 1. Filter and Calculate
            matches = []
            for d in donors:
                if d['blood_group'] == requested_bg:
                    dist = geodesic((h_lat, h_lon), (d['lat'], d['lon'])).km
                    matches.append({**d, "distance_km": round(dist, 2)})

            # 2. Updated Phase 1: Now 5 km
            immediate_donors = [d for d in matches if d['distance_km'] <= 5.0]
            
            # 3. Updated Phase 2: Now 10 km (Including previous donors)
            escalation_donors = [d for d in matches if d['distance_km'] <= 10.0]

            return jsonify({
                "status": "SOS_ACTIVE",
                "immediate_donors": immediate_donors,
                "escalation_donors": escalation_donors
            }), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
# Add this to your existing app.py
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="eblood_bank_app")

# This will store donors registered during the demo session
registered_donors = []

@app.route('/register-donor', methods=['POST'])
def register_donor():
    data = request.json
    pincode = data.get('pincode')
    
    try:
        # Convert Pincode to Lat/Lon
        location = geolocator.geocode(f"{pincode}, India")
        if location:
            new_donor = {
                "id": len(donors) + len(registered_donors) + 1,
                "name": data['name'],
                "blood_group": data['blood_group'],
                "age": data['age'],
                "phone": data['phone'],
                "lat": location.latitude,
                "lon": location.longitude,
                "address": data['address']
            }
            registered_donors.append(new_donor)
            # Add to the main search list as well
            donors.append(new_donor) 
            
            return jsonify({"status": "success", "donor": new_donor}), 200
        else:
            return jsonify({"status": "error", "message": "Invalid Pincode"}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500