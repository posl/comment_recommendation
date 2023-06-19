def solve():
    n,m=map(int,input().split())
    a=[input() for _ in range(2*n)]
    r=[[i+1,0] for i in range(2*n)]
    for i in range(m):
        for j in range(0,2*n,2):
            if a[r[j][0]-1][i]==a[r[j+1][0]-1][i]:
                continue
            elif a[r[j][0]-1][i]=='G' and a[r[j+1][0]-1][i]=='C':
                r[j][1]-=1
            elif a[r[j][0]-1][i]=='C' and a[r[j+1][0]-1][i]=='P':
                r[j][1]-=1
            elif a[r[j][0]-1][i]=='P' and a[r[j+1][0]-1][i]=='G':
                r[j][1]-=1
            else:
                r[j+1][1]-=1
        r.sort(key=lambda x:(x[1],-x[0]))
    for i in range(2*n):
        print(r[i][0])
