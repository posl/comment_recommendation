def main():
    A, B, C = map(int, input().split())
    if C * A > B:
        print(B // A)
    else:
        print(C)
