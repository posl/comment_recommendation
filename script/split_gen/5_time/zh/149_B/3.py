def main():
    A, B, K = map(int, input().split())
    if A >= K:
        A = A - K
    else:
        B = B - (K - A)
        A = 0
        if B < 0:
            B = 0
    print(A, B)
