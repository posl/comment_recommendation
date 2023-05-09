def solve():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 998244353
    ans = [0] * 10
    for a in A:
        ans[a] += 1
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    for m in range(10):
                        if (i + j * k + l * m) % 10 == A[-1]:
                            ans[i] = (ans[i] + ans[j] * ans[k] * ans[l] * ans[m]) % mod
    for i in range(10):
        print(ans[i])
