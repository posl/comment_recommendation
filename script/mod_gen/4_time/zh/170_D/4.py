def solve(n, a):
    a.sort()
    b = [0] * n
    for i in range(n):
        b[i] = a[i]
    for i in range(n):
        if i > 0 and a[i-1] == a[i]:
            b[i] = b[i-1]
        else:
            b[i] = a[i]
    return len(set(b))

if __name__ == '__main__':
    solve()