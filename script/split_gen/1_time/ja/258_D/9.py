def main():
    #入力
    N,X = map(int,input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i],B[i] = map(int,input().split())
    #処理
    #ゲームプレイ時間の総和
    total = 0
    for i in range(N):
        total += B[i]
    #クリア回数
    clear = 0
    #ゲームプレイ時間の総和がXを超えるまでループ
    while total > X:
        #ゲームプレイ時間が最長のステージを探す
        max = 0
        for i in range(N):
            if max < B[i]:
                max = B[i]
                max_index = i
        #ゲームプレイ時間が最長のステージを削除
        total -= max
        B[max_index] = 0
        clear += 1
    #出力
    print(total + clear * A[0])
