from pytz import timezone
from datetime import datetime, timedelta
from utils import get_file_path

TIME_LAG_BTN_TASKS_IN_MINS = 5
LUNCH_TIME = "13:30"
LUNCH_BREAK_IN_MINUTES = 45


class Schedule:
    def get_items(self):
        """
        Returns a list of dicts with name and duration.
        Reads in an input file that is ";" delimented and converts it to a list of dicts
        Returns
            items(list(dict[Name(string), Duration(int)])): dict list
            Sample return
                [{"Name":"Reading", "Duration":"30"}, {{"Name":"Reading", "Duration":"30"}}]
        """
        file_path = get_file_path("input-file.txt")
        items = None
        with open(file_path, "r") as f:
            lines = f.readlines()
            items = [self.get_dict(x) for x in lines]

        return items

    def get_dict(self, item):
        values = item.split(";")
        return {"Name": values[0].strip(), "Duration": float(values[1].strip())}

    def write_schedule(self, schedule):
        """
        write the schedule to a file, this is the case of running the scripts locally
        """

        scheduled = get_file_path(f"schedule.txt")
        f = open(scheduled, "a+")
        f.write(f"\n{datetime.now().strftime('%d/%m/%Y')} Schedule")
        f.write("".join(x for x in schedule))
        f.write("\n")
        f.close()

    def get_item_schedule(self, start_time, item, _timezone="UTC"):
        """
        Using start time create a string to showing the start, end and
        duration of the item
        Returns
            text(str): the string containing the variables named above
            end_time(datetime): end time to be used to get start time for next item
        """
        end_time = start_time + timedelta(minutes=int(item["Duration"]))
        text = (
            f"\n{start_time.astimezone(timezone(_timezone)).strftime('%H:%M')} to "
            f"{end_time.astimezone(timezone(_timezone)).strftime('%H:%M')}"
            f" {item['Name']} {int(item['Duration'])} m"
        )
        return text, end_time

    def get_sorted_items(self):
        items = self.get_items()
        return self.sort_items(items)

    def schedule_items(self, _timezone="UTC"):
        items = self.get_sorted_items()
        start_time = datetime.now()
        scheduled_items = []
        for item in items:
            start_time = start_time + timedelta(minutes=TIME_LAG_BTN_TASKS_IN_MINS)
            text, start_time = self.get_item_schedule(start_time, item, _timezone)
            scheduled_items.append(text)

        return scheduled_items

    def sort_items(self, items):
        """
        items(list(dict)): items contains a dict of items have both "Name" and "Duration"
        Sorts items based on their on their duration in ascending order
        """
        return sorted(items, key=lambda item: item["Duration"])
