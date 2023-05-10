def main():
    import math
    X,Y,R = map(float,input().split())
    X,Y = int(X*10000),int(Y*10000)
    R = int(R*10000)
    ans = 0
    for i in range(X-R,X+R+1):
        if (X-i)**2 > R**2:
            continue
        tmp = math.sqrt(R**2 - (X-i)**2)
        y1 = math.ceil(Y+tmp)
        y2 = math.floor(Y-tmp)
        ans += y1-y2+1
    print(ans)
main()

if __name__ == '__main__':
    main()