def good_integer():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        for j in range(i, N):
            for k in range(j, N):
                if A[i]+A[j]+A[k] <= W:
                    ans += 1
    print(ans)
good_integer()
