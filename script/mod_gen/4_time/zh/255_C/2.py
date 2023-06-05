def solve():
    # x,a,d,n=map(int,input().split())
    x,a,d,n=998244353,-10,-20,30
    if d==0:
        if x==a:
            print(0)
        else:
            print(1)
    elif n==1:
        if x==a:
            print(0)
        else:
            print(1)
    else:
        if d>0:
            if x<a or x>a+(n-1)*d:
                print(1)
            elif (x-a)%d==0:
                print(0)
            else:
                print(1)
        else:
            if x>a or x<a+(n-1)*d:
                print(1)
            elif (x-a)%d==0:
                print(0)
            else:
                print(1)

if __name__ == '__main__':
    solve()