def solve(n, k, td):
    td.sort(key=lambda x: x[1], reverse=True)
    eat = [0] * (n + 1)
    eat_kind = []
    for i in range(k):
        eat[td[i][0]] += 1
        if eat[td[i][0]] == 1:
            eat_kind.append(td[i][0])
    eat_kind.sort()
    ans = sum([t[1] for t in td[:k]])
    ans += len(eat_kind) ** 2
    ans_max = ans
    for i in range(k, n):
        if eat[td[i][0]] == 0:
            eat[td[i][0]] += 1
            eat_kind.append(td[i][0])
        else:
            continue
        eat_kind.sort()
        eat[td[i - k][0]] -= 1
        if eat[td[i - k][0]] == 0:
            eat_kind.remove(td[i - k][0])
        ans = ans - td[i - k][1] + td[i][1] + len(eat_kind) ** 2
        ans_max = max(ans_max, ans)
    return ans_max
n, k = map(int, input().split())
td = [list(map(int, input().split())) for _ in range(n)]
print(solve(n, k, td))
