def joging(a,b,c,d,e,f,x):
    t = 0
    aoki = 0
    takahashi = 0
    while t <= x:
        takahashi += b
        aoki += e
        t += a
        if t > x:
            break
        t += c
        if t > x:
            break
        t += d
        if t > x:
            break
        t += f
    if takahashi > aoki:
        print("Takahashi")
    elif takahashi == aoki:
        print("Draw")
    else:
        print("Aoki")
a,b,c,d,e,f,x = map(int,input().split())
joging(a,b,c,d,e,f,x)

if __name__ == '__main__':
    joging()