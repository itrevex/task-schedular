import datetime
from functions.task_scheduler import Schedule


class TestSchedular:
    def setup_method(self):
        self.schedule = Schedule()

    def test_get_top_hour_start_time(self):
        now = datetime.datetime(2012, 1, 14, 12, 13)
        start_time = self.schedule.get_top_hour_start_time(now)
        assert start_time == datetime.datetime(2012, 1, 14, 12, 15)
