def main():
    N, A, B = map(int, input().split())
    # N, A, B = 8, 3, 4
    # N, A, B = 8, 0, 4
    # N, A, B = 6, 2, 4
    if A == 0:
        print(0)
    elif A == 0 and B == 0:
        print(0)
    elif A + B > N:
        print(N)
    else:
        print(A * (N // (A + B)) + min(A, N % (A + B)))
