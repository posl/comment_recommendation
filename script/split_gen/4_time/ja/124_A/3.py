def main():
    A, B = map(int, input().split())
    if A == B:
        print(A + B)
    else:
        print(max(A + A - 1, B + B - 1, A + B))
