def main():
    N, M = map(int, input().split())
    A = [0 for _ in range(M)]
    B = [0 for _ in range(M)]
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    ans = [0 for _ in range(M)]
    ans[M-1] = (N-1)*N//2
    par = [i for i in range(N+1)]
    size = [1 for _ in range(N+1)]
    def root(x):
        if par[x] == x:
            return x
        else:
            par[x] = root(par[x])
            return par[x]
    def unite(x, y):
        x = root(x)
        y = root(y)
        if x == y:
            return False
        if size[x] < size[y]:
            x, y = y, x
        par[y] = x
        size[x] += size[y]
        return True
    for i in range(M-1, 0, -1):
        ans[i-1] = ans[i]
        if unite(A[i], B[i]):
            ans[i-1] -= size[root(A[i])]*size[root(B[i])]
    for i in range(M):
        print(ans[i])
