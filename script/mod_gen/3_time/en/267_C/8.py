def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    s = sum(a[:m])
    ans = s
    for i in range(n-m):
        s += a[i+m]
        s -= a[i]
        ans = max(ans,s)
    print(ans)

if __name__ == '__main__':
    main()