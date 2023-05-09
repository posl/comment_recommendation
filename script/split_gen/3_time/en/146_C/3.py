def main():
    A, B, X = map(int, input().split())
    if X < A:
        print(0)
        return
    X -= A
    if X / B > 10 ** 9:
        print(10 ** 9)
        return
    X = int(X / B)
    if X == 0:
        print(1)
        return
    print(X)
