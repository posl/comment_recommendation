def main():
    N, M = map(int, input().split())
    K = [0] * M
    S = [[]] * M
    P = [0] * M
    for i in range(M):
        K[i], *S[i] = map(int, input().split())
    P = list(map(int, input().split()))
    ans = 0
    for i in range(2 ** N):
        for j in range(M):
            cnt = 0
            for s in S[j]:
                if (i >> (s - 1)) & 1:
                    cnt += 1
            if cnt % 2 != P[j]:
                break
        else:
            ans += 1
    print(ans)
