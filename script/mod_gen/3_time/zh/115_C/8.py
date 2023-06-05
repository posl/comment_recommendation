def solve():
    N, K = map(int, input().split())
    H = []
    for i in range(N):
        H.append(int(input()))
    H.sort()
    ans = 10**9
    for i in range(N-K+1):
        ans = min(ans, H[i+K-1]-H[i])
    print(ans)

if __name__ == '__main__':
    solve()