def main():
    A, B, C, X = map(int, input().split())
    print((A <= X and X <= A + C) / (B - A))
