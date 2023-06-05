def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(n-m+1):
        ans = max(ans,sum([(i+1)*j for i,j in enumerate(a[i:i+m])]))
    print(ans)

if __name__ == '__main__':
    main()