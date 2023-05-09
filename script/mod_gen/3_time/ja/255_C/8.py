def main():
    x,a,d,n = map(int,input().split())
    if d == 0:
        print(abs(x-a))
    else:
        if x < a:
            if d < 0:
                print(abs(x-a)+abs(a+(n-1)*d))
            else:
                print(abs(x-a))
        elif x > a:
            if d > 0:
                print(abs(x-a)+abs(a+(n-1)*d))
            else:
                print(abs(x-a))
        else:
            print(abs(a+(n-1)*d))

if __name__ == '__main__':
    main()