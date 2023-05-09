def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    #print(len(A))
    #Aの最大値を求める
    max_A = max(A)
    #print(max_A)
    #Aの最大値のindexを求める
    max_index = A.index(max_A)
    #print(max_index)
    #Aの最大値のindexまでの和を求める
    sum_A = sum(A[:max_index+1])
    #print(sum_A)
    #Aの最大値のindexから最後までの和を求める
    sum_A2 = sum(A[max_index+1:])
    #print(sum_A2)
    #Aの最大値のindexまでの和とAの最大値のindexから最後までの和の絶対値の大きい方を出力する
    print(max(sum_A, sum_A2))
