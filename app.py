from flask import Flask, render_template, jsonify
from dotenv import load_dotenv
from goc_api import GolemioClient

load_dotenv()
app = Flask(__name__)
client = GolemioClient()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    try:
        stops_to_track = [
            {"id": "U850Z1P", "name": "Vinohradská tržnice"},
            {"id": "U744Z1P", "name": "Šumavská"}
        ]
        
        all_stops_data = []
        for stop in stops_to_track:
            raw_data = client.get_departure_boards(stop["id"], limit=8)
            processed_departures = []

            for dep in raw_data.get("departures", []):
                t_str = dep["departure_timestamp"]["predicted"].replace(" ", "T")
                
                processed_departures.append({
                    "line": dep["route"]["short_name"],
                    "target": dep["trip"]["headsign"],
                    "timestamp": t_str,
                    "delay_secs": dep["delay"]["seconds"] if dep["delay"]["is_available"] else 0
                })
            
            all_stops_data.append({
                "stop_name": stop["name"],
                "departures": processed_departures
            })
            
        return jsonify(all_stops_data)
    except Exception as e:
        print(f"Chyba na backendu: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)