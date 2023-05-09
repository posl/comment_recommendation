def confusing_time(h, m):
    while True:
        m += 1
        if m == 60:
            h += 1
            m = 0
        if h == 24:
            h = 0
        if str(h)[::-1] == str(m):
            return str(h) + " " + str(m)
            
h, m = map(int, input().split())
print(confusing_time(h, m))
