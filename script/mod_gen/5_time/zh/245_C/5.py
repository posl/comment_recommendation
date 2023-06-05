def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    for i in range(n):
        if abs(a[i]-b[i]) > k:
            print("No")
            exit()
    print("Yes")

if __name__ == '__main__':
    main()