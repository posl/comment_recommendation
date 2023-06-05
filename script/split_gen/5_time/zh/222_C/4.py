def solve():
    n,m = map(int,input().split())
    a = []
    for _ in range(2*n):
        a.append(list(input()))
    rank = [i for i in range(2*n)]
    for i in range(m):
        for j in range(n):
            x = rank[2*j]
            y = rank[2*j+1]
            if a[x][i] == a[y][i]:
                continue
            elif a[x][i] == 'G' and a[y][i] == 'C':
                rank[2*j] = y
                rank[2*j+1] = x
            elif a[x][i] == 'C' and a[y][i] == 'P':
                rank[2*j] = y
                rank[2*j+1] = x
            elif a[x][i] == 'P' and a[y][i] == 'G':
                rank[2*j] = y
                rank[2*j+1] = x
    for i in range(2*n):
        print(rank[i]+1)
