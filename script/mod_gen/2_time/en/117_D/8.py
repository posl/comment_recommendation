def solve(N,K,A):
    # print(N,K,A)
    ans = 0
    for i in range(60,-1,-1):
        if K & (1 << i) == 0:
            continue
        else:
            if ans + (1 << i) > K:
                continue
            else:
                ans += (1 << i)
    # print(ans)
    cnt = [0] * 61
    for i in range(N):
        for j in range(60,-1,-1):
            if A[i] & (1 << j) == 0:
                continue
            else:
                cnt[j] += 1
    # print(cnt)
    ans2 = 0
    for i in range(60,-1,-1):
        if ans & (1 << i) == 0:
            ans2 += (1 << i) * cnt[i]
        else:
            ans2 += (1 << i) * (N - cnt[i])
    print(ans2)

if __name__ == '__main__':
    solve()