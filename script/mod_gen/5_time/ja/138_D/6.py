def main():
    N, Q = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(N-1)]
    queries = [list(map(int, input().split())) for _ in range(Q)]
    # 一つの頂点に対して、その頂点の値と、その頂点の子頂点の値を管理する
    values = [0] * N
    childs = [[] for _ in range(N)]
    for i in range(N-1):
        a, b = edges[i]
        childs[a-1].append(b-1)
    for i in range(Q):
        p, x = queries[i]
        values[p-1] += x
    # 親から子に値を伝播させる
    stack = [0]
    while stack:
        v = stack.pop()
        for c in childs[v]:
            values[c] += values[v]
            stack.append(c)
    print(*values)

if __name__ == '__main__':
    main()