def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    S = [set(s) for s in S]
    alpha = set()
    for s in S:
        alpha |= s
    alpha = list(alpha)
    alpha.sort()
    ans = 0
    for i in range(2 ** len(alpha)):
        cnt = 0
        for j in range(N):
            if sum([1 if alpha[k] in S[j] else 0 for k in range(len(alpha)) if i >> k & 1]) >= K:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)
