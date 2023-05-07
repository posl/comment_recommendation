def nextConfusingTime(h, m):
    if h > 23 or m > 59:
        raise ValueError("h and m must satisfy 0 <= h <= 23 and 0 <= m <= 59")
    if h < 10:
        h = "0" + str(h)
    if m < 10:
        m = "0" + str(m)
    h = str(h)
    m = str(m)
    if h[1] == m[0] and m[1] == h[0]:
        return h + " " + m
    else:
        if m == "59":
            if h == "23":
                h = "00"
            else:
                h = str(int(h) + 1)
                if h < 10:
                    h = "0" + str(h)
        m = str(int(m) + 1)
        if m < 10:
            m = "0" + str(m)
        return nextConfusingTime(h, m)

if __name__ == '__main__':
    nextConfusingTime()