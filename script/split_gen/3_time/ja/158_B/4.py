def main():
    N, A, B = map(int, input().split())
    if A == 0:
        print(0)
    elif A + B == 0:
        print(0)
    else:
        print((N // (A + B)) * A + min(A, N % (A + B)))
