def main():
    N, M = map(int, input().split())
    S = []
    P = []
    for _ in range(M):
        s = list(map(int, input().split()))
        S.append(s[1:])
        P.append(s[0])
    ans = 0
    for i in range(2 ** N):
        flag = True
        for j in range(M):
            cnt = 0
            for k in S[j]:
                if i >> (k - 1) & 1:
                    cnt += 1
            if cnt % 2 != P[j]:
                flag = False
        if flag:
            ans += 1
    print(ans)
