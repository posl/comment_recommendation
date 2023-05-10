def solve():
    N,K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    P = [x-1 for x in P]
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
            tmp = (K//cnt-1)*score
            now = i
            for _ in range(K%cnt):
                now = P[now]
                tmp += C[now]
            ans = max(ans,tmp)
        else:
            tmp = 0
            now = i
            for _ in range(min(K,cnt)):
                now = P[now]
                tmp += C[now]
            ans = max(ans,tmp)
    print(ans)
