def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    # (i,j)に置いて、(i,j)を含む対角線の右上にある黒マスの数
    # 1 <= i <= N, 1 <= j <= N
    # 1-indexed
    black = [[0 for j in range(N+1)] for i in range(N+1)]
    # (i,j)に置いて、(i,j)を含む対角線の右上にある白マスの数
    # 1 <= i <= N, 1 <= j <= N
    # 1-indexed
    white = [[0 for j in range(N+1)] for i in range(N+1)]
    # (i,j)に置いて、(i,j)を含む対角線の右上にある白マスの数
    # 1 <= i <= N, 1 <= j <= N
    # 1-indexed
    white = [[0 for j in range(N+1)] for i in range(N+1)]
    # (i,j)に置いて、(i,j)を含む対角線の右上にある白マスの数
    # 1 <= i <= N, 1 <= j <= N
    # 1-indexed
    white = [[0 for j in range(N+1)] for i in range(N+1)]
    # (i,j)に置いて、(i,j)を含む対角線の右上にある白マスの数
    # 1 <= i <= N, 1 <= j <= N
    # 1-indexed
    white = [[0 for j in range(N+1)] for i in range(N+1)]
    # (i,j)に置いて、(i,j)を含む対角線の右上にある白マスの数
    # 1 <= i <= N, 1 <= j <= N
    # 1
