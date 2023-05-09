def main():
    A, B, K = map(int, input().split())
    if A >= B:
        print(0)
    elif B - A <= K:
        print(0)
    else:
        print(B - A - K)
