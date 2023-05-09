def main():
    N, Q = map(int, input().split())
    par = [i for i in range(N + 1)]
    rank = [0] * (N + 1)
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
    for i in range(Q):
        l = list(map(int, input().split()))
        if l[0] == 1:
            unite(l[1], l[2])
        elif l[0] == 2:
            unite(l[1], l[2])
        else:
            ans = []
            for j in range(1, N + 1):
                if same(l[1], j):
                    ans.append(j)
            print(*ans)

if __name__ == '__main__':
    main()