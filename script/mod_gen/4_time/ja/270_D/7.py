def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(k-1,-1,-1):
        if a[i] <= n:
            ans += n // a[i]
            n %= a[i]
    print(ans)

if __name__ == '__main__':
    main()