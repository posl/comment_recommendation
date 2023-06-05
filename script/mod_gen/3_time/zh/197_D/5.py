def solve(n,x0,y0,xn2,yn2):
    xn1 = (x0+xn2+(yn2-y0)*2**0.5)/2
    yn1 = (y0+yn2+(x0-xn2)*2**0.5)/2
    return xn1,yn1

if __name__ == '__main__':
    solve()