def solution():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = -float('inf')
    for i in range(N):
        score = 0
        pos = i
        cnt = 0
        while cnt < K:
            pos = P[pos] - 1
            score += C[pos]
            cnt += 1
            ans = max(ans, score)
            if pos == i:
                if K % cnt == 0:
                    break
                else:
                    score = score * (K // cnt - 1)
                    cnt = K // cnt * cnt
    print(ans)

if __name__ == '__main__':
    solution()