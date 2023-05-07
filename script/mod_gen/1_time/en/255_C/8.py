def main():
    x,a,d,n=map(int,input().split())
    if d==0:
        print(abs(x-a))
        return
    if n==1:
        print(abs(x-a))
        return
    if d>0:
        if x<a:
            print(min(abs(a-x),abs(a+d*(n-1)-x)))
            return
        if x>a+d*(n-1):
            print(abs(a+d*(n-1)-x))
            return
        print(min(abs(a-x)+d*(n-1),abs(a+d*(n-1)-x)))
        return
    if d<0:
        if x>a:
            print(min(abs(a-x),abs(a+d*(n-1)-x)))
            return
        if x<a+d*(n-1):
            print(abs(a+d*(n-1)-x))
            return
        print(min(abs(a-x)+d*(n-1),abs(a+d*(n-1)-x)))
        return

if __name__ == '__main__':
    main()