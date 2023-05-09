def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    
    ans = 0
    #Aの項を1個以上選ぶ方法は2^N-1通りある
    for i in range(1, 2**N):
        #選んだ項の平均値が整数であるものが何通りかを求める
        #平均値は、選んだ項の合計を選んだ項の個数で割る
        #選んだ項の合計は、選んだ項の2進数表現の1の個数を数えればわかる
        #選んだ項の個数は、選んだ項の2進数表現の1の個数を数えればわかる
        #選んだ項の2進数表現の1の個数を数える
        cnt = 0
        for j in range(N):
            if (i>>j) & 1:
                cnt += 1
        #選んだ項の合計を求める
        sum = 0
        for j in range(N):
            if (i>>j) & 1:
                sum += A[j]
        #選んだ項の合計を選んだ項の個数で割った余りが0になるものを数える
        if sum%cnt == 0:
            ans += 1
    print(ans%MOD)
