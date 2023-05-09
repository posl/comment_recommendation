def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = 0
    cnt = 0
    l = 0
    for r in range(n):
        s += a[r]
        while s >= k:
            cnt += n-r
            s -= a[l]
            l += 1
    print(cnt)

if __name__ == '__main__':
    main()