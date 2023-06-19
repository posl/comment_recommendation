def solve():
    N, W = map(int, input().split())
    A = []
    for _ in range(N):
        s, t, p = map(int, input().split())
        A.append((s, p))
        A.append((t, -p))
    A.sort()
    
    cur = 0
    for _, p in A:
        cur += p
        if cur > W:
            print('No')
            return
    print('Yes')
solve()
