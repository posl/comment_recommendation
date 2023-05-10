def judge_day(day):
    if day == 25:
        return "Christmas"
    elif day == 24:
        return "Christmas Eve"
    elif day == 23:
        return "Christmas Eve Eve"
    elif day == 22:
        return "Christmas Eve Eve Eve"
    else:
        return "Error"

if __name__ == '__main__':
    judge_day()