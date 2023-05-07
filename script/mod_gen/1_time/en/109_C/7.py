def solve():
    N,X = map(int, input().split())
    x = list(map(int, input().split()))
    x.append(X)
    x.sort()
    d = []
    for i in range(N):
        d.append(x[i+1]-x[i])
    d.sort()
    ans = d[0]
    for i in range(N-1):
        ans = gcd(ans,d[i+1])
    print(ans)

if __name__ == '__main__':
    solve()