def solve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    P.sort(reverse=True)
    ans = 0
    for i in range(K):
        ans += P[i]
    ans += K
    ans /= 2
    print(ans)

if __name__ == '__main__':
    solve()