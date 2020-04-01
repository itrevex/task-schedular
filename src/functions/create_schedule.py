from pytz import timezone
from datetime import datetime, timedelta
from utils import get_file_path

TIME_LAG_BTN_TASKS_IN_MINS = 5
LUNCH_TIME = "13:30"
LUNCH_BREAK_IN_MINUTES = 45


class Schedule:
    def get_items(self):
        file_path = get_file_path("input-file.txt")
        items = None
        with open(file_path, "r") as f:
            lines = f.readlines()
            items = [self.get_dict(x) for x in lines]

        return self.sort_items(items)

    def get_dict(self, item):
        values = item.split(";")
        return {"Name": values[0].strip(), "Duration": float(values[1].strip())}

    def schedule_items(self):
        items = self.get_items()
        start_time = datetime.now()
        scheduled = get_file_path(f"schedule.txt")
        scheduled_items = []
        f = open(scheduled, "a+")
        f.write(f"\n{start_time.strftime('%d/%m/%Y')} Schedule")
        for item in items:
            start_time = start_time + timedelta(minutes=TIME_LAG_BTN_TASKS_IN_MINS)
            end_time = start_time + timedelta(minutes=item["Duration"])
            text = (
                f"\n{start_time.astimezone(timezone('Africa/Kampala')).strftime('%H:%M')} to "
                f"{end_time.astimezone(timezone('Africa/Kampala')).strftime('%H:%M')}"
                f" {item['Name']} {int(item['Duration'])} m"
            )
            f.write(text)
            start_time = start_time + timedelta(minutes=item["Duration"])
            scheduled_items.append(text)
        f.write("\n")
        f.close()
        return scheduled_items

    def sort_items(self, items):
        return sorted(items, key=lambda item: item["Duration"])
