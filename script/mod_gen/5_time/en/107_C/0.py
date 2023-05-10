def main():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    ans = float('inf')
    for i in range(n-k+1):
        l = x[i]
        r = x[i+k-1]
        if (l<=0 and r<=0) or (l>=0 and r>=0):
            ans = min(ans, max(abs(l), abs(r)))
        else:
            ans = min(ans, min(abs(l), abs(r))+r-l)
    print(ans)

if __name__ == '__main__':
    main()