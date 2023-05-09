def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = -10 ** 18
    for i in range(N):
        nxt = P[i] - 1
        score = 0
        cnt = 0
        while True:
            cnt += 1
            score += C[nxt]
            if nxt == i:
                break
            nxt = P[nxt] - 1
            if cnt == K:
                break
        if cnt < K and score > 0:
            score *= K // cnt
            ans = max(ans, score)
        ans = max(ans, score)
    print(ans)
