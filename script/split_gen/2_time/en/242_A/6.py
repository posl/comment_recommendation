def main():
    A, B, C, X = map(int, input().split())
    print((B - A + 1) / (B - A + 1 + C) if A <= X <= B else 0)