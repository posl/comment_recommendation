def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[0] % 2 == 0 or a[n-1] % 2 == 0:
        print(-1)
    else:
        print(a[n-1] + a[n-2])

if __name__ == '__main__':
    main()