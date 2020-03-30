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
        now = datetime.now()
        scheduled = get_file_path(f"schedule.txt")
        f = open(scheduled, "a+")
        f.write(f"\n{now.strftime('%d/%m/%Y')} Schedule")
        for item in items:
            now = now + timedelta(minutes=TIME_LAG_BTN_TASKS_IN_MINS)
            f.write(
                f"\n{now.astimezone(timezone('Africa/Kampala')).strftime('%H:%M')}\t{item['Name']}\t{item['Duration']}m"
            )
            now = now + timedelta(minutes=item["Duration"])
        f.write("\n")
        f.close()

    def sort_items(self, items):
        return sorted(items, key=lambda item: item["Duration"])


if __name__ == "__main__":
    Schedule().schedule_items()
