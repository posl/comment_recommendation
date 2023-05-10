def main():
    n,m = map(int,input().split())
    if m == 1:
        print(*[0] + [i for i in range(1,n)])
        for i in range(1,n):
            print(*[i+1 for i in range(1,n)])
        exit()
    ans = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            ans[i][j] = min(i+j,abs(n-i-1)+abs(n-j-1),abs(n-i-1)+j,abs(n-j-1)+i)
    print(*[i for i in ans[0]])
    for i in range(1,n):
        print(*[ans[j][i]+1 for j in range(1,n)])
