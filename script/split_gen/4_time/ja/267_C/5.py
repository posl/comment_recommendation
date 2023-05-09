def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * (n+1)
    for i in range(n):
        b[i+1] = b[i] + a[i]
    c = [0] * (n+1)
    for i in range(n+1):
        c[i] = b[i] - i
    from collections import deque
    q = deque()
    ans = 0
    for i in range(n+1):
        while q and c[q[-1]] >= c[i]:
            q.pop()
        q.append(i)
        if q[0] == i - m:
            q.popleft()
        ans = max(ans, c[i] - c[q[0]])
    print(ans)
main()
