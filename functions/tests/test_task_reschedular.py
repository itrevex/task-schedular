import datetime
import sys
import time
from freezegun import freeze_time

sys.path.append("functions")
from scheduler.reschedule import Reschedule  # noqa

lines = [
    "04/04/2020 Schedule",
    "22:45 to 22:50; read bible; 5 m; 22:50",
    "22:55 to 23:27; more task; 32 m",
    "23:35 to 00:18; other task; 43 m",
    "00:25 to 04:25; moh_corona android; 240 m",
    "",
    "05/04/2020 Schedule",
    "11:30 to 11:35; read bible; 5 m",
    "11:40 to 12:12; more task; 32 m",
    "12:20 to 13:03; other task; 43 m",
    "13:10 to 17:10; moh_corona android; 240 m",
    "",
    "05/04/2020 Schedule",
    "13:40 to 13:45; read bible; 5 m; 14:48",
    "13:50 to 14:22; more task; 32 m",
    "14:30 to 15:13; other task; 43 m",
    "15:20 to 19:20; moh_corona android; 240 m",
]


class TestSchedular:
    def setup_method(self):
        self.schedule = Reschedule()
        pass

    def test_get_top_hour_start_time(self):
        now = datetime.datetime(2012, 1, 14, 12, 13)
        start_time = self.schedule.get_top_hour_start_time(now)
        assert start_time == datetime.datetime(2012, 1, 14, 12, 15)

    def test_gets_last_scheduled_task_line_index(self):
        assert 12 == self.schedule.get_last_task_index(lines)

    def test_get_task_object_from_lines(self):
        now = datetime.datetime(2020, 4, 5, 22, 18)

        task_object = {
            "start_time": now.timestamp(),
            "tasks": [
                {"Name": "more task", "Duration": "32"},
                {"Name": "other task", "Duration": "43"},
                {"Name": "moh_corona android", "Duration": "240"},
            ],
        }

        assert True

    def test_get_name_from_task_string(self):
        line = "13:40 to 13:45; task 1; 5 m;"
        assert self.schedule.get_name_from_task_string(line) == "task 1"

    def test_get_task_lines(self):
        task_lines = [
            "13:40 to 13:45; read bible; 5 m; 14:48",
            "13:50 to 14:22; more task; 32 m",
            "14:30 to 15:13; other task; 43 m",
            "15:20 to 19:20; moh_corona android; 240 m",
        ]
        assert task_lines == self.schedule.get_task_lines(lines)

    def test_get_undone_tasks(self):
        task_lines = [
            "13:50 to 14:22; more task; 32 m",
            "14:30 to 15:13; other task; 43 m",
            "15:20 to 19:20; moh_corona android; 240 m",
        ]
        assert task_lines == self.schedule.get_undone_tasks(lines)

    def test_get_undone_task(self):
        line = "13:40 to 13:45; read bible; 5 m; 14:48"
        assert line == self.schedule.get_done_task(line)
        line = "13:40 to 13:45; read bible; 5 m;"
        assert self.schedule.get_done_task(line) is None
        line = "13:40 to 13:45; read bible; 5 m"
        assert self.schedule.get_done_task(line) is None
