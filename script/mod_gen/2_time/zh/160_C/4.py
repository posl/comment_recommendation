def main():
    k,n = map(int,input().split())
    a = list(map(int,input().split()))
    ans = k
    for i in range(n):
        if i == n-1:
            ans = min(ans,k-a[i]+a[0])
        else:
            ans = min(ans,a[i+1]-a[i])
    print(ans)

if __name__ == '__main__':
    main()