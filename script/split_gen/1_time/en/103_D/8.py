def solve():
    N,M = map(int,input().split())
    AB = [tuple(map(int,input().split())) for _ in range(M)]
    AB.sort()
    ans = 0
    cur = 0
    for a,b in AB:
        if a > cur:
            cur = b - 1
            ans += 1
        elif b <= cur:
            continue
        else:
            cur = b - 1
            ans += 1
    print(ans)
