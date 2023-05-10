def main():
    x,y,r = map(float,input().split())
    x = int(x*10000)
    y = int(y*10000)
    r = int(r*10000)
    ans = 0
    for i in range(x-r,x+r+1):
        if i%10000 != 0:
            continue
        if (r**2-(i-x)**2)**0.5%10000 != 0:
            continue
        ans += 1
    print(ans*2)

if __name__ == '__main__':
    main()