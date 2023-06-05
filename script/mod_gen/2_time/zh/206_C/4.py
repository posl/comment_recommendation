def solve(n):
    s = 0
    for i in range(1, n+1):
        s += i
        if s >= n:
            return i
    return 0

if __name__ == '__main__':
    solve()