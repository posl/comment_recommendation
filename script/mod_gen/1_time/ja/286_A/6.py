def main():
    #入力
    N, P, Q, R, S = map(int, input().split())
    A = list(map(int, input().split()))
    #入れ替え
    B = A[:P-1] + A[Q:R-1] + A[S:] + A[R-1:Q] + A[P-1:R-1]
    #出力
    print(*B)

if __name__ == '__main__':
    main()