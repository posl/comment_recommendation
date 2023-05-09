def main():
    x,a,d,n = map(int,input().split())
    if d==0:
        print(abs(x-a))
        return
    if d>0:
        if x<=a:
            print(a-x)
            return
        if x>=a+d*(n-1):
            print(x-a-d*(n-1))
            return
        print(min(abs(x-a-d*(n-1)),abs(x-a)))
        return
    if d<0:
        if x>=a:
            print(x-a)
            return
        if x<=a+d*(n-1):
            print(a-x-d*(n-1))
            return
        print(min(abs(x-a-d*(n-1)),abs(x-a)))
        return

if __name__ == '__main__':
    main()