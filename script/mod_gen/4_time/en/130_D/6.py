def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    result = 0
    s = 0
    r = 0
    for l in range(n):
        while r < n and s < k:
            s += a[r]
            r += 1
        if s >= k:
            result += n - r + 1
        s -= a[l]
    print(result)

if __name__ == '__main__':
    main()