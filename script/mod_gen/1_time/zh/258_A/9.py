def time_calculator(k):
    if k == 0:
        return "21:00"
    else:
        hour = 21
        minute = 0
        for i in range(k):
            minute += 1
            if minute == 60:
                hour += 1
                minute = 0
            if hour == 24:
                hour = 0
        if hour < 10:
            hour = "0" + str(hour)
        else:
            hour = str(hour)
        if minute < 10:
            minute = "0" + str(minute)
        else:
            minute = str(minute)
        return hour + ":" + minute

if __name__ == '__main__':
    time_calculator()