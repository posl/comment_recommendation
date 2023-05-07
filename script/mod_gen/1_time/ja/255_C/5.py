def main():
    x,a,d,n = map(int,input().split())
    if d == 0:
        print(abs(x-a))
    elif d > 0:
        if x < a:
            print(a-x)
        elif x > a + d*(n-1):
            print(x-(a+d*(n-1)))
        else:
            print(min(x-a,a+d*(n-1)-x))
    else:
        if x > a:
            print(x-a)
        elif x < a + d*(n-1):
            print(a+d*(n-1)-x)
        else:
            print(min(a-x,x-(a+d*(n-1))))

if __name__ == '__main__':
    main()