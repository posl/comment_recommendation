def main():
    n,m = map(int,input().split())
    ans = [[-1 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i==j:
                ans[i][j] = 0
            else:
                if i>j:
                    ans[i][j] = ans[j][i]
    for i in range(n):
        for j in range(n):
            if ans[i][j] == -1:
                ans[i][j] = (i-j)**2
    for i in range(n):
        for j in range(n):
            for k in range(n):
                ans[i][j] = min(ans[i][j],ans[i][k]+ans[k][j])
    for i in range(n):
        for j in range(n):
            if ans[i][j] == 0:
                ans[i][j] = -1
            else:
                ans[i][j] = int(ans[i][j]**0.5)
    for i in range(n):
        print(*ans[i])

if __name__ == '__main__':
    main()