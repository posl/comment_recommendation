def solve(n,m,ab):
    ans = [-1] * n
    for a,b in ab:
        if ans[a-1] == -1:
            ans[a-1] = b
        elif ans[a-1] != b:
            return [-1]
    if ans[0] == -1:
        ans[0] = 1
    for i in range(1,n):
        if ans[i] == -1:
            ans[i] = ans[i-1] + 1
    return ans

if __name__ == '__main__':
    solve()