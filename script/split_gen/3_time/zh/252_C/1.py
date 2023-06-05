def solve():
    n = int(input())
    s = [input() for _ in range(n)]
    ans = float('inf')
    for i in range(n):
        for j in range(10):
            t = 0
            for k in range(n):
                t += min(abs(i-k), n-abs(i-k)) + abs((j-int(s[k][t%10]))%10)
            ans = min(ans, t)
    print(ans)
