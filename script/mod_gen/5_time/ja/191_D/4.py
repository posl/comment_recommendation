def main():
    X,Y,R = map(float,input().split())
    X = int(X*10000)
    Y = int(Y*10000)
    R = int(R*10000)
    cnt = 0
    for i in range(X-R,X+R+1):
        for j in range(Y-R,Y+R+1):
            if (i-X)**2 + (j-Y)**2 <= R**2:
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()