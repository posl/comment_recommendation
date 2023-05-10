def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n-1):
        sum += a[i]
    if n*m - sum > k:
        print(-1)
    else:
        if n*m - sum > 0:
            print(n*m - sum)
        else:
            print(0)

if __name__ == '__main__':
    main()