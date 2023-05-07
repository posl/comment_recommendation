def main():
    N, P, Q, R, S = map(int, input().split())
    A = list(map(int, input().split()))
    #AのP番目からQ番目の項までとR番目からS番目の項までを入れ替えた数列をBとする
    B = A[:P-1] + A[R-1:S] + A[Q:S-1] + A[P-1:R-1] + A[S:]
    print(' '.join(map(str, B)))
