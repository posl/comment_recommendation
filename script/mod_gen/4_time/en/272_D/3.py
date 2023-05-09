def main():
    n, m = map(int, input().split())
    m = m**0.5
    ans = [[-1]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                ans[i][j] = 0
            elif i == 0:
                if ans[i][j-1] != -1 and (m**2 - m**2) == (j-1)**2:
                    ans[i][j] = ans[i][j-1] + 1
            elif j == 0:
                if ans[i-1][j] != -1 and (m**2 - m**2) == (i-1)**2:
                    ans[i][j] = ans[i-1][j] + 1
            else:
                if ans[i-1][j] != -1 and (m**2 - m**2) == (i-1)**2:
                    ans[i][j] = ans[i-1][j] + 1
                if ans[i][j-1] != -1 and (m**2 - m**2) == (j-1)**2:
                    if ans[i][j] == -1:
                        ans[i][j] = ans[i][j-1] + 1
                    else:
                        ans[i][j] = min(ans[i][j], ans[i][j-1] + 1)
    for i in ans:
        print(*i)

if __name__ == '__main__':
    main()