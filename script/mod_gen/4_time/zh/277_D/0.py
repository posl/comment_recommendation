def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    s = sum(a)
    ans = s
    for i in range(n):
        if s > 0 and a[i] >= m:
            break
        s -= a[i]
        ans = min(ans,s + (m - a[i]) % m)
    print(ans)

if __name__ == '__main__':
    main()