def solve():
    n = int(input())
    s = [input() for i in range(n)]
    d = {}
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    ans = 0
    for i in d:
        ans += d[i] * (d[i] - 1) // 2
    print(ans)
solve()
