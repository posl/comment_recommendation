def main():
    n,x,y = map(int,input().split())
    a = list(map(int,input().split()))
    x1 = a[0]
    y1 = 0
    for i in range(1,n):
        r = (x1-x)**2 + (y1-y)**2
        if r == a[i]**2:
            x1 = x
            y1 = y
            continue
        else:
            print("No")
            exit()
    print("Yes")

if __name__ == '__main__':
    main()