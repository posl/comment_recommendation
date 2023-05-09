def calc_days(s):
    days = {
        "Monday": 5,
        "Tuesday": 4,
        "Wednesday": 3,
        "Thursday": 2,
        "Friday": 1,
        "Saturday": 0,
        "Sunday": 6
    }
    return days[s]
