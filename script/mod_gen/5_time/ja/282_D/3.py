def main():
    n,m = map(int,input().split())
    u = []
    v = []
    for i in range(m):
        u_,v_ = map(int,input().split())
        u.append(u_)
        v.append(v_)
    g = [[] for i in range(n+1)]
    for i in range(m):
        g[u[i]].append(v[i])
        g[v[i]].append(u[i])
    c = [0]*(n+1)
    for i in range(1,n+1):
        if c[i] == 0:
            c[i] = 1
            q = [i]
            while q:
                a = q.pop()
                for b in g[a]:
                    if c[b] == 0:
                        c[b] = -c[a]
                        q.append(b)
                    else:
                        if c[b] == c[a]:
                            print(0)
                            exit()
    ans = 0
    for i in range(1,n+1):
        if c[i] == 1:
            ans += 1
    print(ans*(n-ans)-m)
main()

if __name__ == '__main__':
    main()