def problem146a(s):
    week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    return 7 - week.index(s)

if __name__ == '__main__':
    problem146a()