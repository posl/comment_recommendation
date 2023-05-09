def main():
    A, B, C = map(int, input().split())
    if A - B >= C:
        print(C)
    else:
        print(A - B)
