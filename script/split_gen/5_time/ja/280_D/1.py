def solve(k):
    if k % 2 == 0 or k % 5 == 0:
        print(-1)
        return
    n = 1
    while True:
        if n % k == 0:
            print(n)
            return
        n *= 10
        n += 1
        n %= k
