def solve():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.append(X)
    x.sort()
    D = [x[i+1] - x[i] for i in range(N)]
    ans = D[0]
    for i in range(1, N):
        ans = gcd(ans, D[i])
    print(ans)

if __name__ == '__main__':
    solve()