def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = -10**18
    for i in range(N):
        score = 0
        cnt = 0
        cycle = []
        while True:
            score += C[P[i]-1]
            cycle.append(P[i]-1)
            i = P[i]-1
            cnt += 1
            if cnt > K:
                break
            if i == cycle[0]:
                break
        if score <= 0:
            ans = max(ans, max(C))
            continue
        else:
            tmp = score * ((K-cnt)//cnt)
            ans = max(ans, tmp + max(C))
            if (K-cnt) % cnt != 0:
                tmp += sum(C[cycle[0]:(K-cnt)%cnt])
                ans = max(ans, tmp)
    print(ans)
