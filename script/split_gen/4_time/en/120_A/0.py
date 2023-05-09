def main():
    A, B, C = map(int, input().split())
    if A * C > B:
        print(B // A)
    else:
        print(C)
