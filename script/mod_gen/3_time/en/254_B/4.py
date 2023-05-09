def solve(n):
    ans = []
    for i in range(n):
        ans.append([1]*(i+1))
    for i in range(n):
        for j in range(1, i):
            ans[i][j] = ans[i-1][j-1] + ans[i-1][j]
    return ans

if __name__ == '__main__':
    solve()