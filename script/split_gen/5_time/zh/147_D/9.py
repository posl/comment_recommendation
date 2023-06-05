def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    mod = 10**9 + 7
    ans = 0
    for i in range(60):
        num = 0
        for j in range(N):
            if A[j] & (1 << i):
                num += 1
        ans += num * (N - num) * (1 << i)
        ans %= mod
    print(ans)
