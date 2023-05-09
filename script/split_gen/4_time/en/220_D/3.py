def solve():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 998244353
    ans = [0] * 10
    ans[A[0]] = 1
    for i in range(1, N):
        nans = [0] * 10
        for j in range(10):
            nans[(j + A[i]) % 10] += ans[j]
            nans[(j * A[i]) % 10] += ans[j]
        ans = [x % mod for x in nans]
    print(*ans, sep='\n')
