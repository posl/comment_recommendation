def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = [i-1 for i in a]
    # 1回目の移動先
    b = [0] * n
    for i in range(n):
        b[i] = a[i]
    # 2回目の移動先
    c = [0] * n
    for i in range(n):
        c[i] = b[b[i]]
    # 3回目の移動先
    d = [0] * n
    for i in range(n):
        d[i] = c[c[i]]
    # 4回目の移動先
    e = [0] * n
    for i in range(n):
        e[i] = d[d[i]]
    # 5回目の移動先
    f = [0] * n
    for i in range(n):
        f[i] = e[e[i]]
    # 6回目の移動先
    g = [0] * n
    for i in range(n):
        g[i] = f[f[i]]
    # 7回目の移動先
    h = [0] * n
    for i in range(n):
        h[i] = g[g[i]]
    # 8回目の移動先
    i = [0] * n
    for i in range(n):
        i[i] = h[h[i]]
    # 9回目の移動先
    j = [0] * n
    for i in range(n):
        j[i] = i[i][i[i]]
    # 10回目の移動先
    k = [0] * n
    for i in range(n):
        k[i] = j[j[i]]
    # 11回目の移動先
    l = [0] * n
    for i in range(n):
        l[i] = k[k[i]]
    # 12回目の移動先
    m = [0] * n
    for i in range(n):
        m[i] = l[l[i]]
    # 13回目の移動先
    n = [0] * n
    for i in range(n):
        n[i
