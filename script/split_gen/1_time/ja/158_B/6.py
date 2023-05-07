def main():
    N, A, B = map(int, input().split())
    if A == 0 or B == 0:
        print(0)
        return
    if A + B > N:
        print(0)
        return
    if A + B == N:
        print(A)
        return
    if A + B < N:
        if N % (A + B) == 0:
            print(A * (N // (A + B)))
            return
        else:
            print(A * (N // (A + B)) + min(A, N % (A + B)))
            return
