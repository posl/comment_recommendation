def main():
    X,Y,R=map(float,input().split())
    X,Y,R=int(X*10000),int(Y*10000),int(R*10000)
    X1,X2=X-R,X+R
    Y1,Y2=Y-R,Y+R
    ans=0
    for x in range(X1,X2+1):
        for y in range(Y1,Y2+1):
            if (x-X)*(x-X)+(y-Y)*(y-Y)<=R*R:
                ans+=1
    print(ans)

if __name__ == '__main__':
    main()