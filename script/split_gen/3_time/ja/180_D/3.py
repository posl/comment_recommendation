def main():
    x, y, a, b = map(int, input().split())
    ans = 0
    while x < y:
        if x * a < x + b:
            x *= a
        else:
            x += b
        ans += 1
    print(ans - 1)
