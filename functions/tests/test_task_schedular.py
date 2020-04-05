import datetime
import sys

sys.path.append("functions")
from scheduler.task_scheduler import Schedule  # noqa


class TestSchedular:
    def setup_method(self):
        self.schedule = Schedule()
        pass

    def test_get_top_hour_start_time(self):
        now = datetime.datetime(2012, 1, 14, 12, 13)
        start_time = self.schedule.get_top_hour_start_time(now)
        assert start_time == datetime.datetime(2012, 1, 14, 12, 15)

    def test_gets_last_scheduled_task_line_index(self):
        lines = [
            "04/04/2020 Schedule",
            "22:45 to 22:50 read bible 5 m; 22:50",
            "22:55 to 23:27 more task 32 m",
            "23:35 to 00:18 other task 43 m",
            "00:25 to 04:25 moh_corona android 240 m",
            "",
            "05/04/2020 Schedule",
            "11:30 to 11:35 read bible 5 m",
            "11:40 to 12:12 more task 32 m",
            "12:20 to 13:03 other task 43 m",
            "13:10 to 17:10 moh_corona android 240 m",
            "",
            "05/04/2020 Schedule",
            "13:40 to 13:45 read bible 5 m",
            "13:50 to 14:22 more task 32 m",
            "14:30 to 15:13 other task 43 m",
            "15:20 to 19:20 moh_corona android 240 m",
        ]
        assert 12 == self.schedule.get_last_task_index(lines)
