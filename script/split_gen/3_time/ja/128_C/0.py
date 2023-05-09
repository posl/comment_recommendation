def main():
    N, M = map(int, input().split())
    K = []
    S = []
    for i in range(M):
        k, *s = map(int, input().split())
        K.append(k)
        S.append(s)
    P = list(map(int, input().split()))
    ans = 0
    for i in range(2 ** N):
        light = [0] * M
        for j in range(N):
            if (i >> j) & 1:
                for k in range(M):
                    if j + 1 in S[k]:
                        light[k] += 1
        for j in range(M):
            if light[j] % 2 != P[j]:
                break
        else:
            ans += 1
    print(ans)
