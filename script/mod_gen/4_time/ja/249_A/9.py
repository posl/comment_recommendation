def main():
    a,b,c,d,e,f,x = map(int,input().split())
    taka = 0
    aoki = 0
    if a > d:
        taka = x//a
        if x%a > 0:
            taka += 1
    else:
        aoki = x//d
        if x%d > 0:
            aoki += 1
    #print(taka,aoki)
    if taka*b > aoki*e:
        print("Takahashi")
    elif taka*b < aoki*e:
        print("Aoki")
    else:
        print("Draw")

if __name__ == '__main__':
    main()