def solve(n, a):
    # print(n, a)
    # print(a[0], a[1], a[2])
    b = [0 for i in range(n)]
    for i in range(n):
        if i == 0:
            b[i] = a[i] - (a[i+1] + a[n-1]) // 2
        elif i == n-1:
            b[i] = a[i] - (a[0] + a[i-1]) // 2
        else:
            b[i] = a[i] - (a[i+1] + a[i-1]) // 2
    return b

if __name__ == '__main__':
    solve()