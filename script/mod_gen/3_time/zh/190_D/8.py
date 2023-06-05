def solve(n):
    ans = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            m = n // i - i + 1
            if m > 0 and m % 2 == 0:
                ans += 1
    return ans

if __name__ == '__main__':
    solve()