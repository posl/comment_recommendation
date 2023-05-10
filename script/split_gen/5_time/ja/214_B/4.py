def problem214_b():
    s,t = input().split()
    s = int(s)
    t = int(t)
    count = 0
    for a in range(s+1):
        for b in range(s+1):
            for c in range(s+1):
                if a+b+c <= s and a*b*c <= t:
                    count += 1
    print(count)
