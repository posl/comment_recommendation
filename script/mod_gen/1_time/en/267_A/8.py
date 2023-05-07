def days_to_saturday(s):
    days = 0
    while s != "Saturday":
        s = next_day(s)
        days += 1
    return days

if __name__ == '__main__':
    days_to_saturday()