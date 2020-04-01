import os
from cloud_scheduler import CloudScheduler

python_env = os.getenv("PYTHON_ENV", "production")
debug_env = python_env == "development"


def schedule_items(request):
    request_items = get_items(request)
    items = CloudScheduler(request_items).schedule_items()
    return "\n".join(x for x in items)


def get_items(request):
    if debug_env:
        return request
    return request.get_json()
