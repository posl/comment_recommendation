def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    b = []
    for i in range(1,n):
        if a[i] == a[i-1]:
            b.append(a[i])
    if len(b) == 0:
        print(0)
        return
    if b[0] == 0:
        print(m)
        return
    ans = b[0]
    for i in range(1,len(b)):
        ans *= b[i]
        ans %= m
    print(ans)

if __name__ == '__main__':
    main()