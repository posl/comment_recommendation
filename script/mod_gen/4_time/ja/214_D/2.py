def main():
    N = int(input())
    u, v, w = [], [], []
    for i in range(N-1):
        a, b, c = map(int, input().split())
        u.append(a)
        v.append(b)
        w.append(c)
    #print(u)
    #print(v)
    #print(w)
    #print(N)
    #print(len(u))
    #print(len(v))
    #print(len(w))
    ans = 0
    for i in range(N-1):
        for j in range(i+1, N):
            #print(i, j)
            #print(u[i], v[i], w[i])
            #print(u[j], v[j], w[j])
            #print()
            if u[i] == u[j]:
                ans += w[i]
            elif u[i] == v[j]:
                ans += w[i]
            elif v[i] == u[j]:
                ans += w[i]
            elif v[i] == v[j]:
                ans += w[i]
    print(ans)

if __name__ == '__main__':
    main()