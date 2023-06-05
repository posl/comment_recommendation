def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    if a[0] == 0:
        print(-1)
        exit()
    if n == 1:
        print(-1)
        exit()
    for i in range(n-1):
        if a[i] == a[i+1]:
            print(a[i] * 2)
            exit()
    print(-1)

if __name__ == '__main__':
    main()