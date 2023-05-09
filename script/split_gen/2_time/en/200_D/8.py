def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a % 200 for a in A]
    mod = 200
    dp = [0] * mod
    dp[A[0]] = 1
    for i in range(1, N):
        for j in range(mod):
            dp[j] = max(dp[j], dp[(j - A[i]) % mod] + 1)
    if max(dp) < 2:
        print("No")
        return
    else:
        print("Yes")
        dp2 = [0] * mod
        dp2[A[0]] = 1
        for i in range(1, N):
            for j in range(mod):
                dp2[j] = max(dp2[j], dp2[(j - A[i]) % mod] + 1)
            if dp2[A[i]] == 2:
                print("2", i + 1)
                print("1", i + 1)
                return
            if dp2[A[i]] == 1:
                print("1", i + 1)
                for j in range(1, N):
                    if dp2[A[j]] == 2:
                        print("1", j + 1)
                        return
                return
        return
