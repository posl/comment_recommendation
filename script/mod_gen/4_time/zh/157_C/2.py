def main():
    n,m=map(int,input().split())
    s=[0]*m
    c=[0]*m
    for i in range(m):
        s[i],c[i]=map(int,input().split())
    if n==1:
        if m==0:
            print(0)
        elif m==1:
            print(c[0])
        else:
            print(-1)
    elif n==2:
        if m==0:
            print(10)
        elif m==1:
            if s[0]==1:
                print(c[0]*10)
            elif s[0]==2:
                print(c[0]+10)
            else:
                print(-1)
        elif m==2:
            if s[0]==1 and s[1]==2 and c[0]==c[1]:
                print(c[0]*11)
            else:
                print(-1)
        else:
            print(-1)
    elif n==3:
        if m==0:
            print(100)
        elif m==1:
            if s[0]==1:
                print(c[0]*100)
            elif s[0]==2:
                print(c[0]*10+10)
            elif s[0]==3:
                print(c[0]+100)
            else:
                print(-1)
        elif m==2:
            if s[0]==1 and s[1]==2 and c[0]==c[1]:
                print(c[0]*110)
            elif s[0]==1 and s[1]==3 and c[0]==c[1]:
                print(c[0]*101)
            elif s[0]==2 and s[1]==3 and c[0]==c[1]:
                print(c[0]*11+10)
            else:
                print(-1)
        elif m==3:
            if s[0]==1 and s[1]==2 and s[2]==3 and c[0]==c[1] and c[1]==c[2]:
                print(c[0]*111)
            else:
                print(-1)
        else:
            print(-1)
    else:
        print(-1)

if __name__ == '__main__':
    main()