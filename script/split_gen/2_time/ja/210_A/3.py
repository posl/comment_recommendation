def main():
    N, A, X, Y = map(int, input().split())
    if N <= A:
        print(X*N)
    else:
        print(A*X+(N-A)*Y)
