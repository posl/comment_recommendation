def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = -10 ** 9
    for i in range(N):
        score = 0
        cnt = 0
        j = i
        while cnt < K:
            score += C[j]
            j = P[j] - 1
            cnt += 1
            if j == i:
                break
        if cnt == K:
            ans = max(ans, score)
            continue
        m = 0
        j = i
        while j != P[j] - 1:
            m += C[j]
            j = P[j] - 1
        if m <= 0:
            ans = max(ans, score)
            continue
        score += m * ((K - cnt) // cnt)
        ans = max(ans, score)
    print(ans)

if __name__ == '__main__':
    main()