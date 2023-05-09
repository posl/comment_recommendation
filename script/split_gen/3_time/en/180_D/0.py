def main():
    x, y, a, b = map(int, input().split())
    ans = 0
    while x * a < y and x * a - x <= b:
        x *= a
        ans += 1
    ans += (y - 1 - x) // b
    print(ans)
