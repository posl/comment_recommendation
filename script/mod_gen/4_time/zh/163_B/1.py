def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    sum = 0
    for i in range(m):
        sum += a[i]
    if sum <= n:
        print(n - sum)
    else:
        print(-1)

if __name__ == '__main__':
    main()