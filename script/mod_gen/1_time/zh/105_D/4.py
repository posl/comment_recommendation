def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    s = [0]*(n+1)
    for i in range(n):
        s[i+1] = s[i]+a[i]
    d = {}
    for i in range(n+1):
        s[i] %= m
        if s[i] in d:
            d[s[i]] +=1
        else:
            d[s[i]] = 1
    ans = 0
    for i in d:
        ans += d[i]*(d[i]-1)//2
    print(ans)

if __name__ == '__main__':
    main()