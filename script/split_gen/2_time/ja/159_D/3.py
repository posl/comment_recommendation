def main():
    N = int(input())
    A = list(map(int,input().split()))
    #Aの要素の個数を数える
    A_count = [0] * (N+1)
    for i in range(N):
        A_count[A[i]] += 1
    #Aの要素の個数の累積和をとる
    A_sum = [0] * (N+1)
    for i in range(1,N+1):
        A_sum[i] = A_sum[i-1] + A_count[i]
    #Aの要素の個数の累積和を用いて、答えを求める
    for i in range(N):
        ans = A_sum[N] - A_sum[A[i]] + (A_count[A[i]] - 1)
        print(ans)
