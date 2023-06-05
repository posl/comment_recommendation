def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    max_A = A[-1]
    cnt = [0] * (max_A + 1)
    for i in range(N):
        if i == 0:
            cnt[A[i]] = 1
        else:
            if A[i] != A[i - 1]:
                cnt[A[i]] = 1
            else:
                cnt[A[i]] += 1
    ans = [0] * N
    for i in range(1, max_A + 1):
        if cnt[i] == 0:
            continue
        for j in range(i, max_A + 1, i):
            ans[cnt[i] - 1] += cnt[j]
    for i in range(N):
        print(ans[i])
solve()
