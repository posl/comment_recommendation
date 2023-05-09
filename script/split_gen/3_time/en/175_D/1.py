def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = -10**18
    for i in range(N):
        score = 0
        loop = []
        j = i
        while True:
            score += C[j]
            j = P[j] - 1
            loop.append(j)
            if j == i:
                break
        loop_score = 0
        loop_score_max = 0
        for i in range(len(loop)):
            loop_score += C[loop[i]]
            if i < K:
                loop_score_max = max(loop_score_max, loop_score)
            if i >= K:
                loop_score_max = max(loop_score_max, loop_score, loop_score + loop_score_max)
        ans = max(ans, loop_score_max)
    print(ans)
