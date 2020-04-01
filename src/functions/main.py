from .create_schedule import Schedule


def schedule_items(request):
    items = Schedule().schedule_items()
    return "\n".join(x for x in items)
