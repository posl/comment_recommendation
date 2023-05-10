def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0 for _ in range(10)]
    ans[A[0]] = 1
    for a in A[1:]:
        tmp = [0 for _ in range(10)]
        for j in range(10):
            tmp[(j + a) % 10] += ans[j]
            tmp[(j * a) % 10] += ans[j]
            tmp[(j + a) % 10] %= 998244353
            tmp[(j * a) % 10] %= 998244353
        ans = tmp
    for a in ans:
        print(a % 998244353)
