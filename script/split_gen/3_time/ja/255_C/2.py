def main():
    X, A, D, N = map(int, input().split())
    if D == 0:
        print(abs(X-A))
    elif D < 0:
        D = -D
        A = -A
        X = -X
        print(min(abs(X-A), abs(X-A-D*(N-1))))
    else:
        print(min(abs(X-A), abs(X-A-D*(N-1))))
