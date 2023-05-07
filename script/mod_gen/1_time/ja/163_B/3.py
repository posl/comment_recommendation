def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(m):
        n -= a[i]
    if n < 0:
        print(-1)
    else:
        print(n)

if __name__ == '__main__':
    main()