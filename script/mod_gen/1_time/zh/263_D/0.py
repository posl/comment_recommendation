def main():
    n,l,r = map(int,input().split())
    a = list(map(int,input().split()))
    for i in range(n):
        a[i] = a[i] + l
    ans = 0
    for i in range(n):
        ans += a[i]
    a.sort()
    for i in range(n):
        if a[i] > 0:
            break
        if i % 2 == 1:
            ans -= 2 * a[i]
    print(ans)

if __name__ == '__main__':
    main()