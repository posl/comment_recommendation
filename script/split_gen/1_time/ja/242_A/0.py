def main():
    A, B, C, X = map(int, input().split())
    if X <= A:
        print(1)
    elif A < X <= A + C:
        print((C + 1) / (B - A + 1))
    else:
        print(0)
