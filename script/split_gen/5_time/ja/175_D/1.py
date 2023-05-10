def main():
    N,K = map(int,input().split())
    P = list(map(int,input().split()))
    C = list(map(int,input().split()))
    P = [x-1 for x in P]
    ans = -10**18
    for i in range(N):
        score = 0
        cnt = 0
        now = i
        while True:
            now = P[now]
            score += C[now]
            cnt += 1
            if now == i:
                break
            if cnt == K:
                break
        if score > 0:
            m = (K-cnt)//cnt
            score += score*m
        ans = max(ans,score)
    print(ans)
