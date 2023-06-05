def solve(n):
    x = n**(1/3)
    if x.is_integer():
        return int(x)
    else:
        x = int(x)
        while True:
            if x**3+x**2*x+x*x*x+x**3 >= n:
                return x
            x += 1

if __name__ == '__main__':
    solve()