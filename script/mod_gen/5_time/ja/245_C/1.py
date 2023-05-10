def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    flg = True
    for i in range(n):
        if abs(a[i]-b[i]) > k:
            flg = False
            break
    if flg:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()