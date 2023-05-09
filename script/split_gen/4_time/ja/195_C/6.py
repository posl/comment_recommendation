def solve():
    N = int(input())
    if N < 1000:
        print(0)
        return
    ans = 0
    for i in range(1, 16):
        if N < 10 ** (3 * i):
            ans += (i - 1) * (N - 10 ** (3 * (i - 1)) + 1)
            break
        ans += i * (10 ** (3 * i) - 10 ** (3 * (i - 1)))
    print(ans)
