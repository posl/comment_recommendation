def solve(n, q, a, x, k):
    # 用于存储每个数字的索引
    d = {}
    for i in range(n):
        if a[i] not in d:
            d[a[i]] = []
        d[a[i]].append(i + 1)
    # print(d)
    for i in range(q):
        if x[i] not in d:
            print(-1)
        elif len(d[x[i]]) < k[i]:
            print(-1)
        else:
            print(d[x[i]][k[i] - 1])

if __name__ == '__main__':
    solve()