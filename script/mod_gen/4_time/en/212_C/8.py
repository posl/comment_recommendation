def solve(n,m,a,b):
    a.sort()
    b.sort()
    i = 0
    j = 0
    min_diff = 10**9
    while i < n and j < m:
        diff = abs(a[i]-b[j])
        if diff < min_diff:
            min_diff = diff
        if a[i] < b[j]:
            i += 1
        else:
            j += 1
    return min_diff

if __name__ == '__main__':
    solve()