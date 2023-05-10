def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(n-m+1):
        tmp = 0
        for j in range(m):
            tmp += a[i+j]*(j+1)
        ans = max(ans,tmp)
    print(ans)

if __name__ == '__main__':
    main()