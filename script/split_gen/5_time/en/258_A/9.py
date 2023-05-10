def get_time(k):
    # 21:00 JST
    hour = 21
    minute = 0
    # 100 minutes
    minute += k
    # 60 minutes = 1 hour
    hour += minute // 60
    minute = minute % 60
    # 24 hours = 1 day
    hour = hour % 24
    # 1 digit to 2 digits
    hour_str = str(hour)
    minute_str = str(minute)
    if len(hour_str) == 1:
        hour_str = '0' + hour_str
    if len(minute_str) == 1:
        minute_str = '0' + minute_str
    return hour_str + ':' + minute_str
