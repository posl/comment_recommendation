def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0]
    for i in range(n):
        s.append(s[-1] + a[i])
    from collections import deque
    q = deque()
    q.append((0, 0))
    ans = -10**18
    for i in range(1, n + 1):
        while q[0][0] < i - m:
            q.popleft()
        ans = max(ans, s[i] - q[0][1])
        while q and q[-1][1] >= s[i]:
            q.pop()
        q.append((i, s[i]))
    print(ans)

if __name__ == '__main__':
    main()