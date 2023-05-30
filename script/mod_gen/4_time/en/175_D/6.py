def solve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    P = [i-1 for i in P]
    ans = -10**18
    for i in range(N):
        now = i
        score = 0
        cnt = 0
        while True:
            now = P[now]
            score += C[now]
            cnt += 1
            if now == i:
                break
        if score > 0:
            if K < cnt:
                tmp = 0
                now = i
                for j in range(K):
                    now = P[now]
                    tmp += C[now]
                ans = max(ans, tmp)
            else:
                if score > 0:
                    tmp = score * (K//cnt)
                    now = i
                    for j in range(K%cnt):
                        now = P[now]
                        tmp += C[now]
                    ans = max(ans, tmp)
    print(ans)
solve()
