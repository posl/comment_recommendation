def main():
    A, B, X = map(int, input().split())
    if A == 1:
        print(X // B)
        return
    if A * (10 ** 9) + B * 10 < X:
        print(10 ** 9)
        return
    for i in range(1, 10):
        if A * (10 ** i) + B * (i + 1) > X:
            print(10 ** (i - 1) - 1)
            return
    print(10 ** 9)
