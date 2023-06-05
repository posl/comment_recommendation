def solve(n, x, a):
    sum = 0
    for i in range(n):
        if i % 2 == 1:
            sum += a[i] - 1
        else:
            sum += a[i]
    if sum <= x:
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    solve()