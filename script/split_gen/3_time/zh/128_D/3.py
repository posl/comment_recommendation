def solve():
    n, k = map(int, input().split())
    v = list(map(int, input().split()))
    ans = 0
    for i in range(min(n, k) + 1):
        for j in range(min(n, k) + 1):
            if i + j > min(n, k):
                continue
            l = i
            r = k - i - j
            now = 0
            cur = v[:]
            for _ in range(l):
                now += cur.pop(0)
            for _ in range(r):
                now += cur.pop()
            cur.sort()
            for _ in range(j):
                if cur[-1] < 0:
                    cur.pop()
                else:
                    break
            now += sum(cur)
            ans = max(ans, now)
    print(ans)
