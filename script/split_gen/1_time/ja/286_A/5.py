def main():
    #入力
    N, P, Q, R, S = map(int, input().split())
    A = list(map(int, input().split()))
    #出力
    print(*A[:P-1], *A[Q:R-1], *A[S-1:], *A[R-1:Q], *A[P-1:Q])
