def solve(n, v):
    ans = 0
    for i in range(0, n, 2):
        if v[i] == v[i+1]:
            ans += 1
    return ans

if __name__ == '__main__':
    solve()