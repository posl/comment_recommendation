def print_time(k):
    hour = 21 + int(k / 60)
    minute = k % 60
    if hour > 23:
        hour = hour - 24
    if hour < 10:
        hour = "0" + str(hour)
    if minute < 10:
        minute = "0" + str(minute)
    print(str(hour) + ":" + str(minute))
