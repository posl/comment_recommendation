def main():
    a,b,c,d,e,f,x = map(int,input().split())
    #print(a,b,c,d,e,f,x)
    t = 0
    aoki = 0
    takahashi = 0
    while True:
        if t % 2 == 0:
            takahashi += a
        else:
            aoki += d
        if t % 2 == 0:
            if takahashi >= x:
                break
        else:
            if aoki >= x:
                break
        t += 1
        if t % 2 == 0:
            aoki += e
        else:
            takahashi += b
        if t % 2 == 0:
            if aoki >= x:
                break
        else:
            if takahashi >= x:
                break
        t += 1
    if takahashi > aoki:
        print("Takahashi")
    elif takahashi < aoki:
        print("Aoki")
    else:
        print("Draw")

if __name__ == '__main__':
    main()