def main():
    A, B, K = map(int, input().split())
    if B // A >= K:
        print(K)
    else:
        print(B // A)
