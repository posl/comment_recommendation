def main():
    #input
    N, Q = map(int, input().split())
    query = [list(map(int, input().split())) for _ in range(Q)]
    #union-find
    par = list(range(N))
    size = [1]*N
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
            return 0
        else:
            if size[x] < size[y]:
                x, y = y, x
            par[y] = x
            size[x] += size[y]
            return 1
    def same(x, y):
        return find(x) == find(y)
    #solve
    for c, x, y in query:
        x -= 1
        y -= 1
        if c == 1:
            unite(x, y)
        elif c == 2:
            unite(x, y)
            par[y] = y
            size[find(x)] -= 1
        else:
            print(size[find(x)], end=" ")
            for i in range(N):
                if same(i, x):
                    print(i+1, end=" ")
            print()
    return

if __name__ == '__main__':
    main()