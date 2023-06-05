def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    a = sorted(a)
    for i in range(0,n,2):
        if i == 0:
            if a[i] > x:
                print("No")
                return
            else:
                x -= a[i]
        else:
            if a[i]+1 > x:
                print("No")
                return
            else:
                x -= a[i]+1
    print("Yes")

if __name__ == '__main__':
    main()