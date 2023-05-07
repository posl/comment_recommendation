def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    for i in range(N):
        P[i] -= 1
    ans = -10**10
    for i in range(N):
        j = i
        score = 0
        cnt = 0
        loop = []
        while True:
            j = P[j]
            score += C[j]
            loop.append(C[j])
            cnt += 1
            if j == i:
                break
        if score <= 0:
            ans = max(ans, max(loop))
            continue
        if cnt > K:
            ans = max(ans, max(loop))
            continue
        tmp = score * (K // cnt)
        ans = max(ans, tmp)
        if K % cnt == 0:
            continue
        tmp += max(loop[:K % cnt])
        ans = max(ans, tmp)
    print(ans)
