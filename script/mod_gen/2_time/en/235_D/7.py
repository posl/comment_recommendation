def solve(a, N):
    if N == 1:
        return 0
    if N % 2 == 0:
        return 1 + solve(a, N // 2)
    if N % 10 == 1:
        return 1 + solve(a, N // 10)
    return -1
a, N = map(int, input().split())
print(solve(a, N))

if __name__ == '__main__':
    solve()