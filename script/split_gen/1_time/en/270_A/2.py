def main():
    A, B = map(int, input().split())
    print(A + B + max(0, A - 1) + max(0, B - 1))
