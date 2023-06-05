def solve(n, m, k, a, b, c, d):
    # 1. 求出所有的朋友关系
    friends = [[] for _ in range(n + 1)]
    for i in range(m):
        friends[a[i]].append(b[i])
        friends[b[i]].append(a[i])
    # 2. 求出所有的阻隔关系
    blocks = [[] for _ in range(n + 1)]
    for i in range(k):
        blocks[c[i]].append(d[i])
        blocks[d[i]].append(c[i])
    # 3. 求出所有的候选人
    candidates = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j and j not in friends[i] and j not in blocks[i]:
                candidates[i].append(j)
    # 4. 求出每个用户的候选人数
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        ans[i] = len(candidates[i])
    return ans[1:]

if __name__ == '__main__':
    solve()