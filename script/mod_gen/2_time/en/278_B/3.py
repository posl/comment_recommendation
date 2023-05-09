def nextConfusingTime(h, m):
    if h < 10:
        h = "0" + str(h)
    if m < 10:
        m = "0" + str(m)
    time = str(h) + str(m)
    while True:
        if time[0] == time[3] and time[1] == time[2]:
            return time
        m = int(m) + 1
        if m == 60:
            h = int(h) + 1
            m = 0
        if h == 24:
            h = 0
        if h < 10:
            h = "0" + str(h)
        if m < 10:
            m = "0" + str(m)
        time = str(h) + str(m)

if __name__ == '__main__':
    nextConfusingTime()