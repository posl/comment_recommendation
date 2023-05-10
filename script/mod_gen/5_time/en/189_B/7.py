def solve(n, x, v, p):
    sum = 0
    for i in range(n):
        sum += v[i] * p[i]
        if sum > x * 100:
            return i + 1
    return -1

if __name__ == '__main__':
    solve()