def main():
    A, B, K = map(int, input().split())
    if A >= B:
        print(0)
        return
    if A * K >= B:
        print(B - A)
        return
    print(K)
