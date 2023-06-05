def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * (2 * n + 1)
    for i in range(n):
        ans[a[i]] = i + 1
    for i in range(2 * n, 0, -1):
        if ans[i] == 0:
            continue
        if i % 2 == 0:
            ans[i // 2] = ans[i]
        else:
            ans[i // 2] = ans[i] + 1
    for i in range(2 * n + 1):
        print(ans[i])
