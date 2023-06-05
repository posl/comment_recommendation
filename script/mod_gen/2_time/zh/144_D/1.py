def solve(n):
    a = 1
    b = n
    while a < b:
        mid = int((a + b) / 2)
        if mid * mid < n:
            a = mid + 1
        else:
            b = mid
    return a + n - a * a

if __name__ == '__main__':
    solve()