def solve(n,k,h):
    ans = 0
    for i in range(n):
        if h[i] >= k:
            ans += 1
    return ans

if __name__ == '__main__':
    solve()