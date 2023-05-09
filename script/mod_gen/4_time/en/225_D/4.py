def main():
    #input
    n, q = map(int, input().split())
    #initialization
    c = [0]*q
    x = [0]*q
    y = [0]*q
    for i in range(q):
        c[i], x[i], y[i] = map(int, input().split())
    #solve
    #initialize
    par = [i for i in range(n+1)]
    siz = [1]*(n+1)
    #find
    def find(x):
        if par[x] == x:
            return x
        else:
            par[x] = find(par[x])
            return par[x]
    #unite
    def unite(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        if siz[x] < siz[y]:
            x, y = y, x
        siz[x] += siz[y]
        par[y] = x
    #same
    def same(x, y):
        return find(x) == find(y)
    #size
    def size(x):
        return siz[find(x)]
    #query
    for i in range(q):
        if c[i] == 1:
            unite(x[i], y[i])
        elif c[i] == 2:
            unite(x[i], y[i])
            siz[find(x[i])] -= 1
            siz[y[i]] += 1
            par[x[i]] = y[i]
        else:
            print(size(x[i]), end=' ')
            for j in range(1, n+1):
                if same(x[i], j):
                    print(j, end=' ')
            print()

if __name__ == '__main__':
    main()