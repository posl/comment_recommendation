def main():
    N, Q = map(int, input().split())
    # 用邻接表表示树
    tree = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        tree[a-1].append(b-1)
        tree[b-1].append(a-1)
    # 用数组表示计数器
    counter = [0] * N
    for _ in range(Q):
        p, x = map(int, input().split())
        counter[p-1] += x
    # 递归计算计数器
    def dfs(tree, counter, node, parent=None):
        for child in tree[node]:
            if child != parent:
                counter[child] += counter[node]
                dfs(tree, counter, child, node)
    dfs(tree, counter, 0)
    print(*counter)
