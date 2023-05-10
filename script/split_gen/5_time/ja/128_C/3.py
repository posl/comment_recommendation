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
        flag = True
        for j in range(M):
            count = 0
            for k in range(K[j]):
                if i >> (S[j][k] - 1) & 1:
                    count += 1
            if count % 2 != P[j]:
                flag = False
        if flag:
            ans += 1
    print(ans)
