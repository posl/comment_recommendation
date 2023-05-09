def main():
    n,m = map(int,input().split())
    a = []
    for i in range(m):
        a.append(int(input()))
    a.append(n+1)
    a.append(0)
    a.sort()
    b = []
    for i in range(m+2):
        b.append(a[i+1]-a[i]-1)
    b.sort()
    ans = 0
    if b[0] == 0:
        ans = 1
    else:
        ans = 1
        for i in range(m+2):
            if b[i] != 0:
                ans *= fib(b[i])
                ans %= 1000000007
    print(ans)

if __name__ == '__main__':
    main()