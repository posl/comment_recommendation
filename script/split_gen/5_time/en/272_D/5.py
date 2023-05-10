def main():
    n,m = map(int,input().split())
    if n==1:
        print(0)
        return
    if m==1:
        for i in range(n):
            print(i+1)
        return
    #d = [i*i for i in range(1,1000)]
    d = [i*i for i in range(1,1000)]
    d.sort()
    #print(d)
    ans = [[-1 for j in range(n)] for i in range(n)]
    ans[0][0] = 0
    ans[0][1] = 1
    ans[1][0] = 1
    ans[1][1] = 2
    for i in range(2,n):
        ans[0][i] = 2
        ans[i][0] = 2
        ans[1][i] = 3
        ans[i][1] = 3
        ans[i][i] = 4
    for i in range(2,n):
        for j in range(2,i):
            ans[i][j] = 3
            ans[j][i] = 3
    for i in range(2,n):
        for j in range(i+1,n):
            ans[i][j] = 4
            ans[j][i] = 4
    #print(ans)
    for i in range(2,n):
        for j in range(2,i):
            if ans[i][j]==-1:
                if ans[i-1][j]==-1 or ans[i][j-1]==-1:
                    ans[i][j] = 5
                    ans[j][i] = 5
                else:
                    ans[i][j] = ans[i-1][j]+1
                    ans[j][i] = ans[i-1][j]+1
    for i in range(2,n):
        for j in range(i+1,n):
            if ans[i][j]==-1:
                if ans[i-1][j]==-1 or ans[i][j-1]==-1:
                    ans[i][j] = 5
                    ans[j][i] = 5
                else:
                    ans[i][j] = ans[i-1][j]+1
                    ans[j][i] = ans[i-
