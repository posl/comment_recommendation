def main():
    a, b, c = map(int, input().split())
    print((a * (a + 1) * (a + 2) / (a + b + c) / (a + b + c + 1) + b * (b + 1) * (b + 2) / (a + b + c) / (a + b + c + 1) + c * (c + 1) * (c + 2) / (a + b + c) / (a + b + c + 1)) * 100)
