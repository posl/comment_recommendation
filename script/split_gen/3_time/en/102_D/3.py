def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    ans = 10 ** 9
    for i in range(n - 2):
        ans = min(ans, max(s[i + 1], s[n] - s[i + 1]) - min(s[i + 1], s[n] - s[i + 1]))
    for i in range(n - 1):
        ans = min(ans, max(s[i + 1], s[n] - s[i + 1]) - min(s[i + 1], s[n] - s[i + 1]))
    print(ans)
