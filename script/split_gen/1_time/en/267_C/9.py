def main():
    #input
    N, M = map(int, input().split())
    As = list(map(int, input().split()))
    
    #compute
    #前処理
    #As[i]をi+1番目の要素として、累積和を求める
    As = [0] + As
    for i in range(N):
        As[i+1] += As[i]
    
    #最大値の計算
    max_sum = 0
    for i in range(N-M+1):
        max_sum = max(max_sum, As[i+M]-As[i])
    
    #output
    print(max_sum)
