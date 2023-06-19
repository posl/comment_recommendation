def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a = [i%m for i in a]
    a = [0]+a
    for i in range(1,n+1):
        a[i] += a[i-1]
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    ans = 0
    for i in d:
        ans += d[i]*(d[i]-1)//2
    print(ans)

if __name__ == '__main__':
    main()