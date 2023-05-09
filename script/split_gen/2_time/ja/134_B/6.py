def main():
    n, d = map(int, input().split())
    ans = 0
    ans = int(n / (2 * d + 1))
    n = n % (2 * d + 1)
    if n > 0:
        ans += 1
    print(ans)
