def nextSunday(s):
    day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    return (7 - day.index(s)) % 7

if __name__ == '__main__':
    nextSunday()