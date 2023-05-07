def main():
    n, a, b = map(int, input().split())
    s = input()
    ans = 0
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            ans += b
    print(min(ans, (n - 1) * a))
