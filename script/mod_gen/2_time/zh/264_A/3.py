def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n):
        if i > 0:
            a[i] += a[i-1]
    ans = 0
    minsum = 0
    for i in range(n):
        if i > 0:
            minsum = min(minsum, a[i-1])
        if a[i]-minsum < 0:
            ans += l*(a[i]-minsum)
        else:
            ans += r*(a[i]-minsum)
    print(ans)

if __name__ == '__main__':
    main()