def solve(n, p):
    ans = 0
    for i in range(n):
        if i == p[p[i]]:
            ans += 1
    return ans

if __name__ == '__main__':
    solve()