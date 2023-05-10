def main():
    n,m = map(int, input().split())
    roads = []
    for i in range(m):
        roads.append(list(map(int,input().split())))
    #print(roads)
    #f(s,t,k) = min(f(s,t,k-1),f(s,k,k-1) + f(k,t,k-1))
    #f(s,t,0) = c(s,t)
    #c(s,t) = 0 if s=t
    #c(s,t) = c(t,s) if s>t
    #c(s,t) = 0 if s=t
    #c(s,t) = c(t,s) if s>t
    c = [[0 for j in range(n+1)] for i in range(n+1)]
    for i in range(m):
        c[roads[i][0]][roads[i][1]] = roads[i][2]
    #print(c)
    #f(s,t,k) = min(f(s,t,k-1),f(s,k,k-1) + f(k,t,k-1))
    f = [[[0 for k in range(n+1)] for j in range(n+1)] for i in range(n+1)]
    #f(s,t,0) = c(s,t)
    for i in range(1,n+1):
        for j in range(1,n+1):
            f[i][j][0] = c[i][j]
    #print(f)
    #f(s,t,k) = min(f(s,t,k-1),f(s,k,k-1) + f(k,t,k-1))
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                f[i][j][k] = min(f[i][j][k-1],f[i][k][k-1] + f[k][j][k-1])
    #print(f)
    #print( sum_{s = 1}^N sum_{t = 1}^N sum_{k = 1}^N f(s, t, k))
    sum = 0
    for s in range(1,n+1):
        for t in range(1,n+1):
            for k in range(1,n+1):
                sum += f[s][t][k

if __name__ == '__main__':
    main()