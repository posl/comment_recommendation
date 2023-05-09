def solve(N):
    if N == 1:
        return [1]
    else:
        return solve(N-1) + [N] + solve(N-1)
N = int(input())
print(*solve(N))

if __name__ == '__main__':
    solve()