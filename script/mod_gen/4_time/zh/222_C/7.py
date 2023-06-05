def main():
    n,m=map(int,input().split())
    a=[]
    for i in range(2*n):
        a.append(input())
    ans=[]
    for i in range(2*n):
        ans.append([0,i+1])
    for i in range(m):
        for j in range(n):
            p1=ans[2*j][1]-1
            p2=ans[2*j+1][1]-1
            if a[p1][i]==a[p2][i]:
                continue
            elif a[p1][i]=='G' and a[p2][i]=='C':
                ans[2*j][0]-=1
            elif a[p1][i]=='C' and a[p2][i]=='P':
                ans[2*j][0]-=1
            elif a[p1][i]=='P' and a[p2][i]=='G':
                ans[2*j][0]-=1
            else:
                ans[2*j+1][0]-=1
        ans.sort(reverse=True)
    for i in range(2*n):
        print(ans[i][1])
main()
