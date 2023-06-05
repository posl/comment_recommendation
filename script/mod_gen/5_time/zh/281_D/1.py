def main():
    n,k,d = map(int,input().split())
    a = list(map(int,input().split()))
    ans = -1
    for i in range(0,n-k+1):
        s = sum(a[i:i+k])
        if s%d == 0:
            ans = max(ans,s)
    print(ans)

if __name__ == '__main__':
    main()