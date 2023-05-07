def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * 10
    ans[A[0]] = 1
    for i in range(1, N):
        tmp = [0] * 10
        for j in range(10):
            tmp[(j + A[i]) % 10] += ans[j]
            tmp[(j * A[i]) % 10] += ans[j]
            tmp[(j + A[i]) % 10] %= 998244353
            tmp[(j * A[i]) % 10] %= 998244353
        ans = tmp
    for i in range(10):
        print(ans[i])
