def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * 10
    for i in range(10):
        if a[0] == i:
            ans[i] += 1
    for i in range(n - 1):
        tmp = [0] * 10
        for j in range(10):
            if ans[j] == 0:
                continue
            if a[i + 1] == j:
                tmp[j] += ans[j]
            else:
                tmp[(j + a[i + 1]) % 10] += ans[j]
                tmp[(j * a[i + 1]) % 10] += ans[j]
        ans = tmp
    for i in range(10):
        print(ans[i] % 998244353)
