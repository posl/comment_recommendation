def solve(x,y,n):
    if n % 3 == 0:
        return (y / 3) * n
    else:
        return ((y / 3) * (n / 3)) + (x * (n % 3))

if __name__ == '__main__':
    solve()