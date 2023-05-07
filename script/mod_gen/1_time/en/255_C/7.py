def main():
    x,a,d,n = map(int,input().split())
    if d == 0:
        print(abs(x-a))
    elif d > 0:
        if x < a:
            print(a-x)
        elif x > a+d*(n-1):
            print(x-a-d*(n-1))
        else:
            print(min(x-a,x-a-d*(n-1))%d)
    else:
        if x < a+d*(n-1):
            print(a+d*(n-1)-x)
        elif x > a:
            print(x-a)
        else:
            print(min(a-x,a+d*(n-1)-x)%abs(d))

if __name__ == '__main__':
    main()