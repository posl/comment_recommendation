def main():
    n = int(input())
    a = list(map(int, input().split()))
    if a[0] != 1:
        print(-1)
        return
    if n == 1:
        print(0)
        return
    for i in range(n-1):
        if a[i+1] - a[i] != 1:
            print(i+1)
            return
    print(-1)

if __name__ == '__main__':
    main()