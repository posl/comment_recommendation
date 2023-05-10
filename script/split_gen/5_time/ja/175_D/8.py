def solve():
    N, K = map(int, input().split())
    P = [int(x) for x in input().split()]
    C = [int(x) for x in input().split()]
    P = [x - 1 for x in P]
    P = [P[x] for x in P]
    C = [C[x] for x in P]
    #print(P)
    #print(C)
    ans = -10**18
    for i in range(N):
        now = i
        score = 0
        cnt = 0
        while True:
            now = P[now]
            score += C[now]
            cnt += 1
            if cnt >= K:
                break
            if now == i:
                break
        #print(i, now, score, cnt)
        if cnt < K:
            if score > 0:
                max_score = score * (K // cnt - 1)
                if cnt == 1:
                    max_score += score
                else:
                    max_score += score + max(0, score * (K % cnt - 1))
            else:
                max_score = score + max(0, score * (K % cnt - 1))
            ans = max(ans, max_score)
        else:
            ans = max(ans, score)
    print(ans)
