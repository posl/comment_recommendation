def solve():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    for i in range(n):
        if a[i] == 0:
            a[i] = -1
    s = [0]
    for i in range(n):
        s.append(s[-1] + a[i])
    from collections import deque
    q = deque()
    ans = -10**18
    for i in range(n+1):
        while q and s[q[-1]] >= s[i]:
            q.pop()
        q.append(i)
        if i >= m:
            ans = max(ans,s[i] - s[q.popleft()])
    print(ans)
solve()
