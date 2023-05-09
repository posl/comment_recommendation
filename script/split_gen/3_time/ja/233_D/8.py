def main():
    N,K = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N,K,A)
    #print(type(N),type(K),type(A))
    #print(type(A[0]))
    #print("A[0]=",A[0])
    
    #連続部分列の和がKになる組み合わせの個数を求める
    #l,rを固定して、sum(A[l:r+1])を計算する
    #l,rを1つずつ増やしていくと、O(N^2)で計算できるが、TLEになる
    #sum(A[l:r+1]) = sum(A[0:r+1]) - sum(A[0:l])
    #sum(A[0:r+1])を計算しておき、sum(A[0:l])を引くことで、O(N)で計算できる
    #sum(A[0:l])は、sum(A[0:l-1])にA[l-1]を足したものと一致する
    #sum(A[0:l])を計算しておくために、Aの累積和を計算する
    #A[0]は0としておく
    #A[0] = 0
    #A_cum = [0]*(N+1)
    #for i in range(N):
    #    A_cum[i+1] = A_cum[i] + A[i]
    #print(A_cum)
    
    #sum(A[0:l])を計算しておくために、Aの累積和を計算する
    #A[0]は0としておく
    A_cum = [0]
    for i in range(N):
        A_cum.append(A_cum[i] + A[i])
    #print(A_cum)
    
    #sum(A[l:r+1]) = sum(A[0:r+1]) - sum(A[0:l])
    #sum(A[0:r+1]) = K + sum(A[0:l])
    #sum(A[0:l]) = sum(A[0:r+1]) - K
    #sum(A[0:l
