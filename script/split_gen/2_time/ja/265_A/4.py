def main():
    x, y, n = map(int, input().split())
    ans = 0
    if n % 2 == 0:
        ans = n // 2 * min(x * 2, y)
    else:
        ans = (n // 2) * min(x * 2, y) + x
    print(ans)
