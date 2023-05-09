def main():
    N,K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = -10**10
    for i in range(N):
        score = 0
        x = i
        cnt = 0
        while cnt < K:
            x = P[x] - 1
            score += C[x]
            cnt += 1
            if x == i:
                break
        if score <= 0:
            continue
        else:
            if cnt == K:
                ans = max(ans, score)
            else:
                loop = K // cnt
                loop_score = score * loop
                ans = max(ans, loop_score)
                rest = K % cnt
                rest_score = 0
                for j in range(rest):
                    rest_score += C[P[x] - 1]
                    x = P[x] - 1
                    ans = max(ans, loop_score + rest_score)
    print(ans)
