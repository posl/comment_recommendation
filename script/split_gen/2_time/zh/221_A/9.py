def main():
    n = int(input())
    A = list(map(int, input().split()))
    mod = 998244353
    ans = [0] * 10
    for i in range(10):
        ans[i] = 1
    for i in range(n):
        ans2 = [0] * 10
        for j in range(10):
            ans2[(j + A[i]) % 10] += ans[j]
            ans2[(j + A[i]) % 10] %= mod
            ans2[(j * A[i]) % 10] += ans[j]
            ans2[(j * A[i]) % 10] %= mod
        ans = ans2
    for i in range(10):
        print(ans[i])
