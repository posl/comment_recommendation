def main():
    n,k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    ans = 10**9
    for i in range(n-k+1):
        for j in range(n-k+1):
            m = sorted([a[i+x][j+y] for x in range(k) for y in range(k)])
            ans = min(ans, m[k**2//2])
    print(ans)

if __name__ == '__main__':
    main()