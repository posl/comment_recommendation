def main():
    A, B, K = map(int, input().split())
    if A >= K:
        A -= K
    else:
        K -= A
        A = 0
        if B >= K:
            B -= K
    print(A, B)
