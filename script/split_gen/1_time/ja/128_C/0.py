def main():
    N, M = map(int, input().split())
    S = [list(map(int, input().split())) for _ in range(M)]
    P = list(map(int, input().split()))
    ans = 0
    for i in range(2**N):
        flag = 1
        for j in range(M):
            cnt = 0
            for k in range(S[j][0]):
                if ((i >> (S[j][k+1] - 1)) & 1):
                    cnt += 1
            if (cnt % 2) != P[j]:
                flag = 0
                break
        if flag:
            ans += 1
    print(ans)
