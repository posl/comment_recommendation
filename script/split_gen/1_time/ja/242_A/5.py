def main():
    A, B, C, X = map(int, input().split())
    print((1 - ((B - X) / (B - A)) * ((C - 1) / (B - A))) if A <= X <= B else 0)
