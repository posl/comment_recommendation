def solve(n, x, y, a):
    for i in range(n):
        for j in range(i + 1, n):
            if (a[i] + a[j]) % 2 == 1:
                return 'No'
    return 'Yes'

if __name__ == '__main__':
    solve()