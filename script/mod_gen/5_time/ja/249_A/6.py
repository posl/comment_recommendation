def solve():
    a,b,c,d,e,f,x = map(int,input().split())
    t = 0
    while True:
        if t % (c+d) < c:
            x -= a
        else:
            x += b
        if x <= 0:
            print("Aoki")
            break
        if t % (e+f) < e:
            x -= c
        else:
            x += d
        if x <= 0:
            print("Takahashi")
            break
        t += 1

if __name__ == '__main__':
    solve()