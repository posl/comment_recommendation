def main():
    import sys
    input = sys.stdin.readline
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    if n == 1:
        if abs(a[0]-b[0]) <= k:
            print("Yes")
        else:
            print("No")
        exit()
    if n == 2:
        if abs(a[0]-b[0]) <= k and abs(a[1]-b[1]) <= k:
            print("Yes")
            exit()
        if abs(a[0]-a[1]) <= k and abs(b[0]-b[1]) <= k:
            print("Yes")
            exit()
        print("No")
        exit()
    for i in range(n):
        if i == 0:
            if abs(a[i]-b[i]) > k:
                print("No")
                exit()
        elif i == n-1:
            if abs(a[i]-b[i]) > k:
                print("No")
                exit()
            if abs(a[i]-a[i-1]) > k and abs(b[i]-b[i-1]) > k:
                print("No")
                exit()
        else:
            if abs(a[i]-b[i]) > k:
                print("No")
                exit()
            if abs(a[i]-a[i-1]) > k and abs(b[i]-b[i-1]) > k:
                print("No")
                exit()
    print("Yes")

if __name__ == '__main__':
    main()