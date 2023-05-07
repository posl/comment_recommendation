def main():
    N, Q = map(int, input().split())
    # parent[i]: iの親
    parent = [0] * N
    # children[i]: iの子
    children = [[] for _ in range(N)]
    # depth[i]: iの深さ
    depth = [0] * N
    # cnt[i]: iの深さの部分木に含まれる頂点の数
    cnt = [0] * N
    # val[i]: iの深さの部分木に含まれる頂点のカウンターの合計
    val = [0] * N
    for _ in range(N - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        if a > b:
            a, b = b, a
        parent[b] = a
        children[a].append(b)
    stack = [0]
    while stack:
        x = stack.pop()
        for y in children[x]:
            depth[y] = depth[x] + 1
            cnt[y] = 1
            stack.append(y)
    for _ in range(Q):
        p, x = map(int, input().split())
        p -= 1
        val[p] += x
        cnt[p] += 1
    stack = [0]
    while stack:
        x = stack.pop()
        for y in children[x]:
            val[y] += val[x]
            cnt[y] += cnt[x]
            stack.append(y)
    print(*val, sep=' ')
