def solve(n, m, a, b):
    if m == 0:
        return True
    for i in range(m):
        if a[i] == 1:
            if b[i] == 2:
                return False
        elif a[i] == n:
            if b[i] == n-1:
                return False
        elif a[i] == b[i]-1:
            if b[i] == a[i]+1:
                return False
    return True

if __name__ == '__main__':
    solve()