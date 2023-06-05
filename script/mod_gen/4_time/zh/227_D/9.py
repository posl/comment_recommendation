def solve(n, k, a):
    a.sort()
    a.reverse()
    sum = 0
    for i in range(k):
        sum += a[i]
    return sum

if __name__ == '__main__':
    solve()