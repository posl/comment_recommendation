def main():
    N, M = map(int, input().split())
    K = [0] * M
    S = [0] * M
    for i in range(M):
        K[i], *S[i] = map(int, input().split())
    P = list(map(int, input().split()))
    ans = 0
    for i in range(2 ** N):
        cnt = 0
        for j in range(M):
            cnt2 = 0
            for k in range(K[j]):
                if i & (1 << (S[j][k] - 1)):
                    cnt2 += 1
            if cnt2 % 2 == P[j]:
                cnt += 1
        if cnt == M:
            ans += 1
    print(ans)
