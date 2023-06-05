def solve(x,a,d,n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if d == 0:
        if x == a:
            return 0
        else:
            return 1
    if n % 2 == 0:
        return 2
    else:
        return 1

if __name__ == '__main__':
    solve()