from main import schedule_items

data = [
    {"Name": "Item 1", "Duration": "10"},
    {"Name": "Item 2", "Duration": "5"},
    {"Name": "Item 1", "Duration": "120"},
]
if __name__ == "__main__":
    print(schedule_items(data))
