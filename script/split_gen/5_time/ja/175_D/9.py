def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = -10**18
    for i in range(N):
        score = 0
        j = i
        cnt = 0
        while True:
            score += C[j]
            j = P[j] - 1
            cnt += 1
            if j == i:
                break
            if cnt == K:
                break
        if score > ans:
            ans = score
    print(ans)
main()
