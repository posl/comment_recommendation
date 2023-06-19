def  main():
    N = int(input())
    S = [input() for i in range(N)]
    ans = 0
    for i in range(10):
        cnt = [0] * 10
        for j in range(N):
            cnt[int(S[j][i])] += 1
        ans += N - max(cnt)
    print(ans)
