def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * (2 * n + 1)
    for i in range(n):
        ans[a[i]] = i + 1
    for i in range(1, n + 1):
        x = i
        while x != 1:
            ans[x // 2] = max(ans[x // 2], ans[x] + 1)
            x //= 2
    for i in range(1, 2 * n + 1):
        print(ans[i])
