def solve(n, x0, y0, x2, y2):
    return (x0+x2+(y0-y2)*((3**0.5)/3), y0+y2+(x2-x0)*((3**0.5)/3))

if __name__ == '__main__':
    solve()