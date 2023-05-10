def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.append(m)
    d = []
    for i in range(n):
        if a[i+1] - a[i] > 1:
            d.append(a[i+1] - a[i] - 1)
    if len(d) == 0:
        print(0)
    else:
        d.sort()
        k = d[0]
        ans = 0
        for i in d:
            ans += (i+k-1)//k
        print(ans)

if __name__ == '__main__':
    main()