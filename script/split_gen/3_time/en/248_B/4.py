def main():
    A, B, K = map(int, input().split())
    if A >= B:
        print(0)
    else:
        print(max(0, min(B - A - 1, K)))
