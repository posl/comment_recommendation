def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if k == 1:
        if a == sorted(a):
            print("Yes")
        else:
            print("No")
    else:
        for i in range(1, n-k+1):
            if a[i-1] > a[i+k-1]:
                print("Yes")
                return
        print("No")

if __name__ == '__main__':
    main()