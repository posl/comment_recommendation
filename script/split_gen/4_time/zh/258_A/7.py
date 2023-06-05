def print_time(k):
    hour = 21
    minute = 0
    if k < 60:
        minute = minute + k
    else:
        hour = hour + int(k / 60)
        minute = minute + k % 60
    if minute >= 60:
        hour = hour + 1
        minute = minute - 60
    if hour >= 24:
        hour = hour - 24
    print(str(hour).zfill(2) + ':' + str(minute).zfill(2))
