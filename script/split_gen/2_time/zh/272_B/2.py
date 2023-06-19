def main():
    n,m = map(int,input().split())
    a = [[0 for i in range(n)] for j in range(n)]
    for i in range(m):
        x = list(map(int,input().split()))
        for j in range(1,len(x)):
            for k in range(j+1,len(x)):
                a[x[j]-1][x[k]-1] = 1
                a[x[k]-1][x[j]-1] = 1
    for i in range(n):
        for j in range(i+1,n):
            if a[i][j] == 0:
                print('No')
                exit()
    print('Yes')
