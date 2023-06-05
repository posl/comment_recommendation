def main():
    x,y,r = map(float,input().split())
    x = int(x*10000)
    y = int(y*10000)
    r = int(r*10000)
    r2 = r*r
    ans = 0
    for i in range(-r,r+1):
        j = r2 - i*i
        if j>=0:
            j = int(j**0.5)
            ans += j//10000 +1
    print(ans*4)

if __name__ == '__main__':
    main()