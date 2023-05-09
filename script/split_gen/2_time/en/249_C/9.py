def main():
    import sys
    N, K = map(int, input().split())
    S = [set(input()) for _ in range(N)]
    ans = 0
    for i in range(1 << N):
        cnt = 0
        tmp = set()
        for j in range(N):
            if i & (1 << j):
                cnt += 1
                tmp |= S[j]
        if cnt == K:
            ans = max(ans, len(tmp))
    print(ans)
