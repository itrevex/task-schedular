from datetime import timedelta


class Common:
    def get_top_hour_start_time(self, start_time):
        minutes = start_time.minute
        additional_minutes = 5 - (minutes % 5)
        # this means we got a modulus of zero and no need to add extra minutes
        if additional_minutes != 5:
            start_time = start_time + timedelta(minutes=additional_minutes)
        return start_time
