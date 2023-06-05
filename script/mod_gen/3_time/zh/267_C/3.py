def solve():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    s = [0]
    for i in range(n):
        s.append(s[-1]+a[i])
    from collections import deque
    q = deque()
    q.append((0,0))
    res = -float("inf")
    for i in range(1,n+1):
        while q and q[0][0] < i-m:
            q.popleft()
        res = max(res,s[i]-q[0][1])
        while q and q[-1][1] >= s[i]:
            q.pop()
        q.append((i,s[i]))
    print(res)

if __name__ == '__main__':
    solve()