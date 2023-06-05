def main():
    a, b, c, d = map(int, input().split())
    if a < b:
        print(-1)
        return
    if d == 1:
        print(0)
        return
    if a <= c * d:
        print(1)
        return
    print((a - c * d - 1) // (b - c) + 1 + 1)
