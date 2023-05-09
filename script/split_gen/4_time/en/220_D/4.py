def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 998244353
    ans = [0] * 10
    for i in range(10):
        for j in range(N):
            if A[j] == i:
                ans[i] += 1
    for i in range(1, N):
        ans2 = [0] * 10
        for j in range(10):
            for k in range(10):
                ans2[(j + k) % 10] += ans[j] * ans[k]
                ans2[(j * k) % 10] += ans[j] * ans[k]
        ans = ans2
    for i in range(10):
        print(ans[i] % mod)
