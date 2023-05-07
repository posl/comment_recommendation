def solve():
    a,b,h,m = map(int,input().split())
    a = a/12
    b = b/60
    h = h + m/60
    h = h*5
    h = h*6
    m = m*6
    h = h - m
    h = h * math.pi / 180
    ans = (a**2 + b**2 - 2*a*b*math.cos(h))**0.5
    print(ans)

if __name__ == '__main__':
    solve()