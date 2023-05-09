def problem():
    s,t = map(int, input().split())
    count = 0
    for i in range(s+1):
        for j in range(s+1-i):
            for k in range(s+1-i-j):
                if i*j*k <= t:
                    count += 1
    print(count)
problem()
