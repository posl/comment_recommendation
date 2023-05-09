def main():
    X, Y, N = map(int, input().split())
    # print(X, Y, N)
    # print(type(X), type(Y), type(N))
    # print(X * (N % 3) + Y * (N // 3))
    print(X * (N % 3) + Y * (N // 3))
