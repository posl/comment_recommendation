def main():
    x, y, n = map(int, input().split())
    ans = n // 3 * y
    if n % 3 == 1:
        ans += x
    elif n % 3 == 2:
        ans += y
    print(ans)
