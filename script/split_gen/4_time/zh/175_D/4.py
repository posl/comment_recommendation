def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = -10**18
    for i in range(N):
        now = i
        score = 0
        cnt = 0
        while True:
            now = P[now] - 1
            score += C[now]
            cnt += 1
            if now == i:
                break
            if cnt == K:
                break
        if cnt < K:
            if score > 0:
                score += (K // cnt - 1) * score
            for j in range(K % cnt):
                now = P[now] - 1
                score += C[now]
        ans = max(ans, score)
    print(ans)
