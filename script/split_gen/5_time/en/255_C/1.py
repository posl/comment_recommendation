def main():
    X, A, D, N = map(int, input().split())
    if D == 0:
        if A == X:
            print(0)
        else:
            print("inf")
        return
    if D > 0:
        if X < A or X > A + D * (N - 1):
            print(0)
            return
        if (X - A) % D == 0:
            print((X - A) // D)
        else:
            print("inf")
        return
    if D < 0:
        if X > A or X < A + D * (N - 1):
            print(0)
            return
        if (X - A) % D == 0:
            print((X - A) // D)
        else:
            print("inf")
        return
