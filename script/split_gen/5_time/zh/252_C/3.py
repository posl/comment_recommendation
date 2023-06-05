def solve():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    ans = 0
    for i in range(10):
        for j in range(n):
            cnt = 0
            for k in range(n):
                if s[j][i] == s[k][i]:
                    cnt += 1
            ans = max(ans, cnt)
    print(ans)
solve()
