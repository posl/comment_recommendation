def solve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = -10 ** 18
    for i in range(N):
        score = 0
        cur = i
        for _ in range(K):
            cur = P[cur] - 1
            score += C[cur]
            ans = max(ans, score)
            if cur == i: break
    print(ans)

if __name__ == '__main__':
    solve()