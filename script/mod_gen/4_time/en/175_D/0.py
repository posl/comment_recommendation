def solve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    P = [p - 1 for p in P]
    ans = -10 ** 18
    for i in range(N):
        score = 0
        v = i
        for _ in range(K):
            v = P[v]
            score += C[v]
            ans = max(ans, score)
            if v == i:
                break
    return ans
print(solve())

if __name__ == '__main__':
    solve()