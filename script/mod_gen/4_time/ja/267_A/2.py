def calc_days(s):
    days = 0
    if s == "Monday":
        days = 5
    elif s == "Tuesday":
        days = 4
    elif s == "Wednesday":
        days = 3
    elif s == "Thursday":
        days = 2
    elif s == "Friday":
        days = 1
    return days

if __name__ == '__main__':
    calc_days()