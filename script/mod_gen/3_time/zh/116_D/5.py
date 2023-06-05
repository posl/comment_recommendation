def solve():
    n, k = map(int, input().split())
    t_d = []
    for i in range(n):
        t, d = map(int, input().split())
        t_d.append((t, d))
    t_d.sort(key=lambda x: x[1], reverse=True)
    t_d.sort(key=lambda x: x[0])
    # print(t_d)
    d = 0
    t_set = set()
    for i in range(k):
        d += t_d[i][1]
        t_set.add(t_d[i][0])
    # print(d, t_set)
    ans = d + len(t_set) ** 2
    # print(ans)
    for i in range(k, n):
        if t_d[i][0] not in t_set:
            d += t_d[i][1] - t_d[k - 1][1]
            t_set.add(t_d[i][0])
            ans = max(ans, d + len(t_set) ** 2)
    print(ans)

if __name__ == '__main__':
    solve()