def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n-1):
        sum += a[i]
    if n*m - sum <= k:
        print(max(n*m - sum, 0))
    else:
        print(-1)

if __name__ == '__main__':
    main()