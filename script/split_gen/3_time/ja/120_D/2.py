def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
        A[i] -= 1
        B[i] -= 1
    # 連結成分の個数
    ans = [0] * M
    ans[M-1] = N * (N-1) // 2
    # 各連結成分のサイズ
    size = [1] * N
    # 連結成分の根
    root = list(range(N))
    def root_of(x):
        if root[x] == x:
            return x
        else:
            root[x] = root_of(root[x])
            return root[x]
    def unite(x, y):
        x = root_of(x)
        y = root_of(y)
        if x == y:
            return
        ans[M-1] -= size[x] * size[y]
        if size[x] < size[y]:
            x, y = y, x
        root[y] = x
        size[x] += size[y]
    for i in range(M-1, 0, -1):
        ans[i-1] = ans[i]
        if root_of(A[i]) != root_of(B[i]):
            ans[i-1] -= 1
            unite(A[i], B[i])
    for i in range(M):
        print(ans[i])
