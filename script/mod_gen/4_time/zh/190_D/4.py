def solve(N):
    ans = 0
    for i in range(1, int(N ** 0.5) + 1):
        if N % i == 0:
            m = N // i - i + 1
            if m % 2 == 0:
                ans += 1
    return ans * 2

if __name__ == '__main__':
    solve()