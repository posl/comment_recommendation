def main():
    N, A, B = map(int, input().split())
    if N == 1:
        if A == 0 and B == 0:
            print(0)
        else:
            print(1)
    else:
        if A == 0 and B == 0:
            print(0)
        else:
            print((N // (A + B)) * A + min(N % (A + B), A))
