def solve():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = [0] * 10
    ans[A[0]] = 1
    for i in range(1, N):
        new_ans = [0] * 10
        for j in range(10):
            new_ans[(j + A[i]) % 10] += ans[j]
            new_ans[(j + A[i]) % 10] %= MOD
            new_ans[(j * A[i]) % 10] += ans[j]
            new_ans[(j * A[i]) % 10] %= MOD
        ans = new_ans
    for i in range(10):
        print(ans[i])
