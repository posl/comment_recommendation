def get_days_to_saturday(s):
    days = 0
    if s == "星期一":
        days = 5
    elif s == "星期二":
        days = 4
    elif s == "星期三":
        days = 3
    elif s == "星期四":
        days = 2
    elif s == "星期五":
        days = 1
    return days

if __name__ == '__main__':
    get_days_to_saturday()