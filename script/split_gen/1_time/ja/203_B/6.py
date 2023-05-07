def main():
    #入力
    N, K = map(int, input().split())
    #変数
    sum = 0
    #処理
    for i in range(1, N+1):
        for j in range(1, K+1):
            sum += i*100 + j
    #出力
    print(sum)
