def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    total = 0
    for i in range(n):
        if i % 2 == 1:
            total += a[i] - 1
        else:
            total += a[i]
    if total <= x:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()