def main():
    a,b,c,d,e,f,x = map(int, input().split())
    t = 0
    h = 0
    while True:
        if t >= x:
            break
        t += 1
        if t % (a + b) <= a and t % (d + e) <= d:
            h += 1
        elif t % (a + b) <= a:
            h += 1
        elif t % (d + e) <= d:
            continue
        else:
            continue
    if h == 0:
        print("Draw")
    elif h == t:
        print("Draw")
    elif h > t / 2:
        print("Takahashi")
    else:
        print("Aoki")

if __name__ == '__main__':
    main()