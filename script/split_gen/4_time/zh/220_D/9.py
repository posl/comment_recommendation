def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * 10
    ans[A[0]] += 1
    for i in range(N - 1):
        B = [0] * 10
        for j in range(10):
            B[(j + A[i + 1]) % 10] += ans[j]
            B[(j * A[i + 1]) % 10] += ans[j]
        ans = B
    for i in range(10):
        print(ans[i] % 998244353)
