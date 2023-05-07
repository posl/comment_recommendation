def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * 10
    for i in range(10):
        ans[i] = 0
    ans[A[0]] = 1
    for i in range(1, N):
        tmp = [0] * 10
        tmp[A[i]] += 1
        for j in range(10):
            tmp[(j + A[i]) % 10] += ans[j]
            tmp[(j * A[i]) % 10] += ans[j]
        ans = tmp
    for i in range(10):
        print(ans[i] % 998244353)
