def solve(n, x, a, b):
    for i in range(n):
        if x == a[i] or x == b[i]:
            return 'Yes'
    return 'No'

if __name__ == '__main__':
    solve()