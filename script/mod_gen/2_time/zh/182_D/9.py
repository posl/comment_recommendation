def solve(n, a):
    max = 0
    sum = 0
    for i in range(0, n):
        sum += a[i]
        if sum > max:
            max = sum
    return max

if __name__ == '__main__':
    solve()