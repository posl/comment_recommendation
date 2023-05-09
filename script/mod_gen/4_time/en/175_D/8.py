def solve(N, K, P, C):
    max_score = -10**10
    for i in range(N):
        score = 0
        cnt = 0
        j = i
        while cnt < K:
            cnt += 1
            j = P[j] - 1
            score += C[j]
            max_score = max(max_score, score)
            if j == i:
                break
    return max_score
N, K = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))
print(solve(N, K, P, C))

if __name__ == '__main__':
    solve()