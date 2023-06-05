def get_time(k):
    hour = 21
    minute = 0
    while k > 0:
        minute += 1
        if minute == 60:
            hour += 1
            minute = 0
        if hour == 24:
            hour = 0
        k -= 1
    return str(hour).zfill(2) + ':' + str(minute).zfill(2)
