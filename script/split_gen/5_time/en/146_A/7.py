def get_days_to_next_sunday(day):
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    return 7 - days.index(day)
