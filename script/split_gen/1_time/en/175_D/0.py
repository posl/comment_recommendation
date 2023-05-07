def main():
    N, K = [int(x) for x in input().split()]
    P = [int(x) for x in input().split()]
    C = [int(x) for x in input().split()]
    ans = -10**10
    for i in range(N):
        tmp = 0
        now = i
        for j in range(K):
            now = P[now]-1
            tmp += C[now]
            if tmp <= 0:
                break
            if now == i:
                ans = max(ans, (K-j-1)//j*tmp+tmp)
                break
            ans = max(ans, tmp)
    print(ans)
