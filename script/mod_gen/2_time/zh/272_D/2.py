def main():
    n,m = map(int,input().split())
    ans = [[-1 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                ans[i][j] = 0
            elif i == 0:
                ans[i][j] = ans[i][j-1]+1
            elif j == 0:
                ans[i][j] = ans[i-1][j]+1
            else:
                ans[i][j] = min(ans[i-1][j],ans[i][j-1])+1
    for i in range(n):
        for j in range(n):
            if ans[i][j] == -1:
                print(ans[i][j],end=" ")
            else:
                print(ans[i][j]*2,end=" ")
        print()

if __name__ == '__main__':
    main()