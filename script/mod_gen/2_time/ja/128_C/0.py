def main():
    N, M = map(int, input().split())
    K = []
    S = []
    P = []
    for _ in range(M):
        k, *s = map(int, input().split())
        K.append(k)
        S.append(s)
    P = list(map(int, input().split()))
    ans = 0
    for i in range(2 ** N):
        flag = True
        for j in range(M):
            cnt = 0
            for k in range(K[j]):
                if (i >> (S[j][k] - 1) & 1):
                    cnt += 1
            if cnt % 2 != P[j]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)
main()
