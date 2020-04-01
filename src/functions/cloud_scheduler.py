from task_scheduler import Schedule


class CloudScheduler(Schedule):
    def __init__(self, data):
        self.request = data

    def get_items(self):
        return self.request
