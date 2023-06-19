def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * 10
    for i in range(10):
        ans[i] = a.count(i)
    for i in range(1, n):
        tmp = [0] * 10
        for j in range(10):
            for k in range(10):
                tmp[(j + k) % 10] += ans[j] * a[k]
                tmp[(j * k) % 10] += ans[j] * a[k]
        ans = tmp
    for i in range(10):
        print(ans[i] % 998244353)
