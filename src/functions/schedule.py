from task_scheduler import Schedule

if __name__ == "__main__":
    scheduler = Schedule()
    items = scheduler.schedule_items("Africa/Kampala")
    scheduler.write_schedule(items)
