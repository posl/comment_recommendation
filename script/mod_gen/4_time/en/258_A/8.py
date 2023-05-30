def time_after_21(k):
    hour = 21 + int(k/60)
    minute = k%60
    if hour >= 24:
        hour = hour - 24
    if hour < 10:
        hour = '0' + str(hour)
    if minute < 10:
        minute = '0' + str(minute)
    return str(hour) + ':' + str(minute)
print(time_after_21(63))
print(time_after_21(45))
print(time_after_21(100))
