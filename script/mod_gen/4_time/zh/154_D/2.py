def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    p2 = [0]*(n+1)
    for i in range(n):
        p2[i+1] = p2[i] + p[i]
    ans = 0
    for i in range(n-k+1):
        ans = max(ans,(p2[i+k]-p2[i]+k)/2)
    print(ans)

if __name__ == '__main__':
    main()