def solve(N):
    ans = 0
    for i in range(1, int(N ** (1/3)) + 1):
        for j in range(i, int((N / i) ** (1/2)) + 1):
            if i == j:
                ans += 1
            else:
                ans += 3
    return ans

if __name__ == '__main__':
    solve()