import re
from .common import Common


class Reschedule(Common):
    def get_last_task_index(self, lines):
        """
        Get last line index after being passed lines from a read file
        """
        last_index = None
        for i, line in enumerate(lines):
            if re.search(r"schedule$", str(line).lower()):
                last_index = i
        return last_index

    def get_name_from_task_string(self, line):
        value = line.split(";")[1].strip()
        return value

    def get_done_task(self, line):
        try:
            undone_task = line.split(";")[3].strip()
            if re.search(r"^\d{2}:\d{2}", undone_task):
                return line
        except IndexError:
            pass

    def get_task_lines(self, lines):
        last_schedule_index = self.get_last_task_index(lines) + 1
        scheduled_lines = lines[last_schedule_index:]
        return scheduled_lines

    def get_undone_tasks(self, lines):
        task_lines = self.get_task_lines(lines)
        undone_task_lines = []
        for line in task_lines:
            done_line = self.get_done_task(line)
            if not done_line:
                undone_task_lines.append(line)

        return undone_task_lines
