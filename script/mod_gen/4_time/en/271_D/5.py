def solve(n, s, a, b):
    for i in range(1 << n):
        sum = 0
        for j in range(n):
            if i & (1 << j):
                sum += a[j]
            else:
                sum += b[j]
        if sum == s:
            return i
    return -1

if __name__ == '__main__':
    solve()