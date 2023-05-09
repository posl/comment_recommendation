def problem():
    k = int(input())
    n = 1
    while True:
        if n > k:
            print(-1)
            break
        elif (n * (n + 1)) % k == 0:
            print(n + 1)
            break
        n += 1
problem()
