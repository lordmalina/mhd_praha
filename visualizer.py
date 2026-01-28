from datetime import datetime

class Visualizer:
    def __init__(self):
        self.now = datetime.now().astimezone()

    def visualize_departure_board(self, data):
        departures_list = data.get("departures", [])

        result = f"{'Linka:':<8} | {'Cíl:':<20} | {'Odjezd za:':<12} | {'Zpoždění:'}\n"
        result += ("-" * 60) + "\n"

        for departure in departures_list:
            line = departure["route"]["short_name"]
            destination = departure["trip"]["headsign"]
            

            pred_time_str = departure["departure_timestamp"]["predicted"].replace(" ", "")
            pred_time = datetime.fromisoformat(pred_time_str)
            

            diff = pred_time - self.now
            total_seconds = int(diff.total_seconds())
            

            if total_seconds > 0:
                mins, secs = divmod(total_seconds, 60)
                wait_time_fmt = f"{mins:02d}:{secs:02d}"
            else:
                wait_time_fmt = "00:00"

            if departure["delay"]["is_available"]:
                delay_total_secs = departure["delay"]["seconds"]
                abs_delay = abs(delay_total_secs)
                d_mins, d_secs = divmod(abs_delay, 60)
                
                sign = "+" if delay_total_secs >= 0 else "-"
                delay_fmt = f"{sign}{d_mins:02d}:{d_secs:02d}"
            else:
                delay_fmt = "+00:00"

            result += f"{line:<8} | {destination:<20} | {wait_time_fmt:<12} | {delay_fmt}\n"

        return result