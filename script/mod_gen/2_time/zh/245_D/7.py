def solve(n, k, a, b):
    for i in range(n):
        if abs(a[i] - b[i]) > k:
            return 'No'
    return 'Yes'

if __name__ == '__main__':
    solve()