def main():
    a,b,c,d,e,f,x = map(int,input().split())
    taka = 0
    aoki = 0
    while True:
        if taka + a > x:
            print("Takahashi")
            break
        else:
            taka += a
        if aoki + d > x:
            print("Aoki")
            break
        else:
            aoki += d
        if taka + b > x:

if __name__ == '__main__':
    main()