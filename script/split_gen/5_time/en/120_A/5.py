def main():
    A, B, C = map(int, input().split())
    if C < B // A:
        print(C)
    else:
        print(B // A)
