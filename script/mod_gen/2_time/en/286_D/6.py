def solve(n, x, a, b):
    sum = 0
    for i in range(n):
        sum += a[i] * b[i]
        if sum > x:
            return False
    if sum < x:
        return False
    return True

if __name__ == '__main__':
    solve()