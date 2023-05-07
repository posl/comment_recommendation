def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    #A[i]を含む部分列の個数
    C = [0] * N
    #A[i]を含む部分列の個数の累積和
    S = [0] * N
    #A[i]を含む部分列の個数の累積和の最大値
    M = [0] * N
    for i in range(N):
        if i == 0:
            C[i] = 1
            S[i] = 1
            M[i] = 1
        else:
            if A[i] == A[i-1]:
                C[i] = C[i-1]
                S[i] = S[i-1] + C[i]
                M[i] = max(M[i-1], S[i])
            else:
                C[i] = 1
                S[i] = S[i-1] + C[i]
                M[i] = max(M[i-1], S[i])
    #print(A)
    #print(C)
    #print(S)
    #print(M)
    #A[i]を含む部分列の個数の累積和の最大値がK以上の場合、A[i]を含む部分列の個数はK以上
    #A[i]を含む部分列の個数の累積和の最大値がK未満の場合、A[i]を含む部分列の個数はK未満
    #A[i]を含む部分列の個数の累積和の最大値がK以上の場合、A[i]を含む部分列の個数はK以上
    #A[i]を含む部分列の個数の累積和の最大値がK未満の場合、A[i]を含む部分列の個数はK未満
    #A[i]
