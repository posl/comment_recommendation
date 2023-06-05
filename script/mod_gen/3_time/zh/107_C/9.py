def main():
    n,k = map(int,input().split())
    x = list(map(int,input().split()))
    x.sort()
    ans = 10**9
    for i in range(n-k+1):
        l = x[i]
        r = x[i+k-1]
        ans = min(ans,abs(l)+abs(r-l),abs(r)+abs(l-r))
    print(ans)

if __name__ == '__main__':
    main()