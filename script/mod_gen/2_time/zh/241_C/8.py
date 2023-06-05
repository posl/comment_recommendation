def solve(n, m, a, b):
    if m > n:
        return False
    a.sort()
    b.sort()
    for i in range(m):
        if a[-1-i] < b[-1-i]:
            return False
    return True

if __name__ == '__main__':
    solve()