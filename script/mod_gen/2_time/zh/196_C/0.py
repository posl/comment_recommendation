def solve(N):
    if N < 10:
        return 0
    if N < 100:
        return 1
    if N < 1000:
        return 9
    if N < 10000:
        return 9 + 1
    if N < 100000:
        return 9 + 1 + 9
    if N < 1000000:
        return 9 + 1 + 9 + 1
    if N < 10000000:
        return 9 + 1 + 9 + 1 + 9
    if N < 100000000:
        return 9 + 1 + 9 + 1 + 9 + 1
    if N < 1000000000:
        return 9 + 1 + 9 + 1 + 9 + 1 + 9
    if N < 10000000000:
        return 9 + 1 + 9 + 1 + 9 + 1 + 9 + 1
    if N < 100000000000:
        return 9 + 1 + 9 + 1 + 9 + 1 + 9 + 1 + 9
    if N < 1000000000000:
        return 9 + 1 + 9 + 1 + 9 + 1 + 9 + 1 + 9 + 1
    if N < 10000000000000:
        return 9 + 1 +

if __name__ == '__main__':
    solve()