def main():
    global N, Q, a, b, p, x, tree, ans
    N, Q = map(int, input().split())
    a = [0]*N
    b = [0]*N
    p = [0]*Q
    x = [0]*Q
    tree = [[] for i in range(N)]
    ans = [0]*N
    for i in range(N-1):
        a[i], b[i] = map(int, input().split())
        a[i] -= 1
        b[i] -= 1
        tree[a[i]].append(b[i])
        tree[b[i]].append(a[i])
    for i in range(Q):
        p[i], x[i] = map(int, input().split())
        p[i] -= 1
    dfs(0, -1)
    print(" ".join(map(str, ans)))
