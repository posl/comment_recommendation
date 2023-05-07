def main():
    N = int(input())
    a = list(map(int, input().split()))
    #aの中の値をインデックスに持つリストを作成
    a_index = [0] * (N+1)
    for i in range(N):
        a_index[a[i]] = i
    #連続する数列の長さを格納するリスト
    length_list = [0] * (N+1)
    #aの中の値をインデックスに持つリストを左から順に見ていく
    for i in range(1, N+1):
        #aの中の値がインデックスと一致する場合
        if a_index[i] == i-1:
            #連続する数列の長さを格納するリストのインデックスをインクリメント
            length_list[i] += 1
        #aの中の値がインデックスと不一致の場合
        else:
            #連続する数列の長さを格納するリストのインデックスをインクリメント
            length_list[i] += 1
            #連続する数列の長さを格納するリストのインデックスをインクリメント
            length_list[a_index[i]+1] -= 1
    #連続する数列の長さの累積和を格納するリスト
    cumsum = [0] * (N+1)
    #連続する数列の長さの累積和を計算
    for i in range(1, N+1):
        cumsum[i] = cumsum[i-1] + length_list[i]
    #条件を満たす組の個数
    count = 0
    #連続する数列の長さの累積和を格納するリストを左から順に見ていく
    for i in range(1, N+1):
        #連続する数列の長さがインデックスと一
