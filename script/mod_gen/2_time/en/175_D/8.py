def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = -10**18
    for i in range(N):
        x = i
        score = 0
        loop = []
        for j in range(K):
            x = P[x] - 1
            score += C[x]
            loop.append(C[x])
            if x == i:
                break
        if score <= 0 or len(loop) == K:
            ans = max(ans, score)
            continue
        loop_score = sum(loop)
        loop_count = (K - len(loop)) // len(loop)
        ans = max(ans, score + loop_score * loop_count)
        loop_score = loop_score * (loop_count + 1)
        loop = loop * (loop_count + 1)
        for j in range(K - len(loop)):
            loop_score += loop[j]
            ans = max(ans, loop_score)
    print(ans)

if __name__ == '__main__':
    main()