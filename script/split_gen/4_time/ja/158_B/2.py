def main():
    N, A, B = map(int, input().split())
    if N % (A + B) == 0:
        print(A * (N // (A + B)))
    else:
        print(A * (N // (A + B)) + min(A, N % (A + B)))
