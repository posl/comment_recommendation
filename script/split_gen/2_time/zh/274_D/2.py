def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * (2 * n + 1)
    for i in range(n):
        ans[a[i]] = i + 1
    for i in range(2, 2 * n + 1):
        ans[i] = ans[i // 2] + 1
    for i in range(1, 2 * n + 1):
        print(ans[i])
