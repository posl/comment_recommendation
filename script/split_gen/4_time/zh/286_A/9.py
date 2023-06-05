def main():
    N, P, Q, R, S = map(int, input().split())
    A = list(map(int, input().split()))
    B = []
    B.extend(A[P-1:Q])
    B.extend(A[R-1:S])
    B.extend(A[Q:R-1])
    B.extend(A[S:])
    print(' '.join(map(str, B)))
