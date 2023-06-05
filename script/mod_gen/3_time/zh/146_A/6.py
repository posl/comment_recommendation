def next_day(day):
    if day == "SUN":
        return 7
    elif day == "MON":
        return 6
    elif day == "TUE":
        return 5
    elif day == "WED":
        return 4
    elif day == "THU":
        return 3
    elif day == "FRI":
        return 2
    elif day == "SAT":
        return 1

if __name__ == '__main__':
    next_day()