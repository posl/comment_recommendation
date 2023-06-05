def solve(n, a, b):
    sum = 0
    for i in range(n):
        sum += (b[i] - a[i] + 1) * (b[i] + a[i]) / 2
    return sum

if __name__ == '__main__':
    solve()