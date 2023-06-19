def main():
    x,y,r = map(float,input().split())
    x = int(x*10000)
    y = int(y*10000)
    r = int(r*10000)
    r2 = r*r
    ans = 0
    for i in range(x-r,x+r+1):
        for j in range(y-r,y+r+1):
            if (i-x)*(i-x)+(j-y)*(j-y)<=r2:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()