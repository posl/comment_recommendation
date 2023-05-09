def main():
    n, m = map(int, input().split())
    drinks = []
    for _ in range(n):
        a, b = map(int, input().split())
        drinks.append((a, b))
    drinks.sort()
    ans = 0
    for a, b in drinks:
        if m >= b:
            ans += a * b
            m -= b
        else:
            ans += a * m
            break
    print(ans)
