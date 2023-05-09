def main():
    N, P, Q, R, S = map(int, input().split())
    A = list(map(int, input().split()))
    B = A[P-1:Q] + A[R-1:S]
    print(*B)
