def is_chaotic_time(time):
    hour = time // 100
    minute = time % 100
    if hour < 0 or hour > 23 or minute < 0 or minute > 59:
        return False
    else:
        if hour < 10:
            hour = "0"+str(hour)
        if minute < 10:
            minute = "0"+str(minute)
        if str(hour)[::-1] == str(minute):
            return True
        else:
            return False
