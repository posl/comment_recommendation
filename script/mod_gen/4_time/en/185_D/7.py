def main():
    n, m = map(int, input().split())
    if m == 0:
        print(1)
        return
    a = list(map(int, input().split()))
    a.sort()
    b = []
    b.append(a[0]-1)
    for i in range(1, m):
        b.append(a[i]-a[i-1]-1)
    b.append(n-a[m-1])
    b.sort()
    k = b[0]
    ans = 0
    for i in range(m+1):
        if b[i] % k == 0:
            ans += b[i] // k
        else:
            ans += b[i] // k + 1
    print(ans)

if __name__ == '__main__':
    main()