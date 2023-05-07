def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    ans = [0] * M
    ans[M - 1] = (N - 1) * N // 2
    par = [0] * (N + 1)
    rank = [0] * (N + 1)
    for i in range(1, N + 1):
        par[i] = i
        rank[i] = 0
    def find(x):
        if par[x] == x:
            return x
        else:
            par[x] = find(par[x])
            return par[x]
    def unite(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        if rank[x] < rank[y]:
            par[x] = y
        else:
            par[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1
    def same(x, y):
        return find(x) == find(y)
    for i in range(M - 1, 0, -1):
        ans[i - 1] = ans[i]
        if not same(A[i], B[i]):
            ans[i - 1] -= (rank[find(A[i])] + 1) * (rank[find(B[i])] + 1)
            unite(A[i], B[i])
    for i in range(M):
        print(ans[i])

if __name__ == '__main__':
    main()