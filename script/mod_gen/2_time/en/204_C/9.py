def main():
    # Initialization
    N, M = map(int, input().split())
    # A_i, B_i
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    # Union Find
    par = [i for i in range(N+1)]
    rank = [0 for _ in range(N+1)]
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
    # Union Find
    for a, b in AB:
        unite(a, b)
    # Count
    cnt = 0
    for i in range(1, N+1):
        if par[i] == i:
            cnt += 1
    # Output
    print(cnt*(cnt-1))

if __name__ == '__main__':
    main()