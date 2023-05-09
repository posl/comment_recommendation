def solve(n, x, y, a):
    for i in range(n):
        for j in range(i+1, n):
            if a[i] + a[j] == abs(x - y):
                return True
    return False

if __name__ == '__main__':
    solve()