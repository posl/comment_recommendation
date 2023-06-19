def main():
    N, M = map(int, input().split())
    K = [0] * M
    S = [[0] * N for _ in range(M)]
    P = [0] * M
    for i in range(M):
        t = list(map(int, input().split()))
        K[i] = t[0]
        S[i] = t[1:]
    P = list(map(int, input().split()))
    ans = 0
    for i in range(2 ** N):
        flag = True
        for j in range(M):
            cnt = 0
            for k in range(K[j]):
                if i & (1 << (S[j][k] - 1)):
                    cnt += 1
            if cnt % 2 != P[j]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)
main()
