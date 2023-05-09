def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    P = [p - 1 for p in P]
    ans = -10 ** 18
    for i in range(N):
        j = P[i]
        score = C[j]
        for _ in range(K - 1):
            j = P[j]
            score += C[j]
            ans = max(ans, score)
    print(ans)
