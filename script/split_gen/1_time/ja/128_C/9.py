def main():
    N,M = map(int,input().split())
    S = [0]*M
    P = [0]*M
    for i in range(M):
        S[i] = list(map(int,input().split()))
        S[i].pop(0)
    P = list(map(int,input().split()))
    ans = 0
    for i in range(2**N):
        flag = True
        for j in range(M):
            cnt = 0
            for k in S[j]:
                if (i >> (k-1)) & 1:
                    cnt += 1
            if cnt % 2 != P[j]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)
