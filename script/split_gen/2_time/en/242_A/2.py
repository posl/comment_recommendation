def main():
    A, B, C, X = map(int, input().split())
    print((B - X + 1) / (B - A + 1) * C / (B - A + 1 - C))
