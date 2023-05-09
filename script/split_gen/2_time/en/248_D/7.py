def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    # Aの要素をindexに、Aの要素の出現回数をvalueにした辞書を作成
    A_dict = {}
    for i in range(N):
        if A[i] in A_dict:
            A_dict[A[i]] += 1
        else:
            A_dict[A[i]] = 1
    # Q個のクエリについて、Aの要素の出現回数を出力
    for i in range(Q):
        L, R, X = map(int, input().split())
        if X in A_dict:
            print(A_dict[X])
        else:
            print(0)
