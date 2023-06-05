def solve():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[0])
    from collections import deque
    q = deque()
    ans = 0
    i = 0
    for day in range(1, m + 1):
        while i < n and ab[i][0] == day:
            q.append(ab[i][1])
            i += 1
        if q:
            ans += max(q)
            q.remove(max(q))
    print(ans)
solve()
