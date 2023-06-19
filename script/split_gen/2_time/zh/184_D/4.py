def main():
    a, b, c = map(int, input().split())
    print((a * (a + b + c - 1) + b * (b + c - 1) + c * (c - 1)) / (a + b + c - 1))
