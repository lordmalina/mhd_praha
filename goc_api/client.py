import os
import requests
from datetime import datetime

class GolemioClient:
    def __init__(self):
        self.base_url = "https://api.golemio.cz/v2"
        self.api_key = os.getenv("api_key")
        self.headers = {
            "accept": "application/json",
            "X-Access-Token": self.api_key
        }

    def get_stop_by_id(self, stop_id: str) -> str:
        url = f"{self.base_url}/gtfs/stops"
        params = {"ids": stop_id}
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()
    
    def get_trip_by_stop_id(self, stop_id: str, date: str = None, limit: int = None) -> str:
        url = f"{self.base_url}/gtfs/trips"
        params = {"stopId": stop_id,
                  "date": date,
                  "limit": limit}
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    def get_departure_boards(self, stop_id: str, mins_before: int = 0, mins_after: int = 60, time_from: datetime = None, limit: int = 10) -> str:
        if time_from is None:
            time_from = datetime.now()
            
        url = f"{self.base_url}/pid/departureboards"
        params = {
            "ids": stop_id,
            "minutesBefore": mins_before,
            "minutesAfter": mins_after,
            "timeFrom": time_from.isoformat(),
            "limit": limit
        }
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()