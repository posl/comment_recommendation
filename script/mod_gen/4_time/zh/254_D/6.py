def solve(n):
    ans = 0
    for i in range(1, n+1):
        for j in range(i, n+1):
            if i * j > n:
                break
            elif i == j:
                ans += 1
            else:
                ans += 2
    return ans

if __name__ == '__main__':
    solve()