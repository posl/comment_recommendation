def confusing_time(h, m):
    while True:
        m += 1
        if m == 60:
            m = 0
            h += 1
            if h == 24:
                h = 0
        if str(h).count('2') + str(h).count('5') + str(m).count('2') + str(m).count('5') == 4:
            return str(h) + ':' + str(m)
