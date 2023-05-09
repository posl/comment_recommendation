def solve():
    N = int(input())
    ans = 0
    for p in range(2, int(N ** 0.25) + 1):
        if N % p == 0:
            q = N // p
            if q % p ** 3 == 0:
                ans += 1
    print(ans)
