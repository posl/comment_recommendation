def main():
    x,a,d,n = map(int,input().split())
    if d == 0:
        if x == a:
            print(0)
        else:
            print(1)
        return
    if n == 1:
        if x == a:
            print(0)
        else:
            print(1)
        return
    if n == 2:
        if x == a or x == a+d:
            print(0)
        else:
            print(1)
        return
    if (x-a)%d == 0:
        print(0)
    else:
        print(1)

if __name__ == '__main__':
    main()