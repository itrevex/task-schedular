from pytz import timezone
from datetime import datetime, timedelta
from utils.files import get_file_path
from .common import Common

TIME_LAG_BTN_TASKS_IN_MINS = 5
LUNCH_TIME = "13:30"
LUNCH_BREAK_IN_MINUTES = 45


class Schedule(Common):
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
            items = [self.get_dict(x) for x in lines if x.strip("\n") != ""]

        return items

    def get_dict(self, item):
        values = item.split(";")
        priority = 0
        try:
            priority = values[2].strip()
        except IndexError:
            pass
        return {
            "Name": values[0].strip(),
            "Duration": float(values[1].strip()),
            "Priority": int(priority if priority != "" else 0),
        }

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
            f"{end_time.astimezone(timezone(_timezone)).strftime('%H:%M')};"
            f" {item['Name']}; {int(item['Duration'])} m;"
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
            start_time = self.get_top_hour_start_time(start_time)
            text, start_time = self.get_item_schedule(start_time, item, _timezone)
            scheduled_items.append(text)

        return scheduled_items

    def sort_items(self, items):
        """
        items(list(dict)): items contains a dict of items have both "Name" and "Duration"
        Sorts items based on their on their duration in ascending order

        Logic
        Sort item based on top priority, get sorted sort list and resort items that have similar 
        priority level for the already sorted priority and resort them and plack them back into list
        """

        priority_sort = sorted(items, key=lambda item: item["Priority"])
        duration_sort = self.get_second_degree_sort(
            priority_sort, "Priority", "Duration"
        )
        return duration_sort

    def get_second_degree_sort(self, items, sorted_key, required_sort):
        second_degree_sort = []
        similar_items = [items[0]]
        for i in range(len(items)):
            if i == 0:
                continue
            if self.is_equal_to_previous(items, sorted_key, i):
                similar_items.append(items[i])
            else:
                second_degree_sort.extend(
                    sorted(similar_items, key=lambda item: item[required_sort])
                )
                similar_items = [items[i]]

            if i == len(items) - 1:
                # this is the last item, sort whatever is in the similar items list and move on
                second_degree_sort.extend(
                    sorted(similar_items, key=lambda item: item[required_sort])
                )
        return second_degree_sort

    def is_equal_to_previous(self, items, key, i):
        prev_item = items[i - 1][key]
        current_item = items[i][key]
        return prev_item == current_item

    def get_task_object(self, lines, last_schedule_index):
        pass
