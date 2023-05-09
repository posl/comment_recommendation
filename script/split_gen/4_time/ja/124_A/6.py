def main():
    A, B = map(int, input().split())
    if A >= B:
        print(A + max(A - 1, B))
    else:
        print(B + max(A, B - 1))
