def main():
    n,k = map(int,input().split())
    x = list(map(int,input().split()))
    x.sort()
    if k == n:
        print(0)
        return
    elif k == 1:
        print(x[-1] - x[0])
        return
    else:
        ans = 10**9
        for i in range(n-k+1):
            ans = min(ans,x[i+k-1]-x[i]+min(abs(x[i]),abs(x[i+k-1])))
        print(ans)
        return

if __name__ == '__main__':
    main()