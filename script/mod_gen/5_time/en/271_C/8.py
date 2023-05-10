def solve(n, a):
    a.sort()
    a.reverse()
    i = 0
    while i < n:
        if a[i] <= i:
            return i
        i += 1
    return i

if __name__ == '__main__':
    solve()