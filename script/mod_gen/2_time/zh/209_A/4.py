def main():
    #读入数据
    n,m = map(int,input().split())
    a,b,c = [0]*m,[0]*m,[0]*m
    for i in range(m):
        a[i],b[i],c[i] = map(int,input().split())
    #初始化
    d = [[float('inf')]*n for i in range(n)]
    for i in range(n):
        d[i][i] = 0
    for i in range(m):
        d[a[i]-1][b[i]-1] = c[i]
    #Floyd-Warshall算法
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k]+d[k][j])
    #计算结果
    result = 0
    for s in range(n):
        for t in range(n):
            for k in range(n):
                if d[s][t] == d[s][k]+d[k][t]:
                    result += d[s][t]
    print(result)

if __name__ == '__main__':
    main()