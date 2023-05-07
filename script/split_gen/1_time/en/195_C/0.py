def main():
    n = int(input())
    ans = 0
    i = 1
    while i <= n:
        ans += (n - i + 1)
        i *= 1000
    print(ans)
