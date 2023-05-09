def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[0] != 1:
        print(-1)
        return
    for i in range(n-1):
        if a[i+1] - a[i] > 1:
            print(-1)
            return
    print(n - a.count(a[0]))

if __name__ == '__main__':
    main()