def solve(n):
    MOD = 10**9 + 7
    return (10**n - 2*9**n + 8**n) % MOD
print(solve(int(input())))

if __name__ == '__main__':
    solve()