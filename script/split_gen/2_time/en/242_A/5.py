def main():
    a, b, c, x = map(int, input().split())
    print((min(x - 1, b - a) - max(0, x - c - a) + 1) / (b - a + 1))
