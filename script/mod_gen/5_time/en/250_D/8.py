def solve():
    N = int(input())
    if N < 2:
        print(0)
        return
    p = int(N ** 0.25)
    q = int(N ** 0.5)
    ans = 0
    while p > 1:
        while q > p:
            t = p * q * q * q
            if t <= N:
                ans += 1
            q -= 1
        p -= 1
        q = int(N ** 0.5)
    print(ans)

if __name__ == '__main__':
    solve()