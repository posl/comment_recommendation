def solve(n, s, a, b):
    for i in range(1 << n):
        sum = 0
        for j in range(n):
            if (i >> j) & 1:
                sum += a[j]
            else:
                sum += b[j]
        if sum == s:
            return True, i
    return False, -1

if __name__ == '__main__':
    solve()