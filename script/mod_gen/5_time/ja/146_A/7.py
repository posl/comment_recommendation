def get_next_sunday(s):
    if s == "SUN":
        return 7
    elif s == "MON":
        return 6
    elif s == "TUE":
        return 5
    elif s == "WED":
        return 4
    elif s == "THU":
        return 3
    elif s == "FRI":
        return 2
    elif s == "SAT":
        return 1

if __name__ == '__main__':
    get_next_sunday()