def main():
    S = input()
    K = int(input())
    if K == 0:
        print(S.count("X"))
        return
    #Sの先頭にXを追加
    S = "X" + S
    #Sの末尾にXを追加
    S = S + "X"
    #Sの連続したXの数をカウントする
    cnt = 0
    cnt_list = []
    for s in S:
        if s == "X":
            cnt += 1
        else:
            cnt_list.append(cnt)
            cnt = 0
    #print(cnt_list)
    #cnt_listの中の最大値を求める
    #cnt_listが空の場合は0を出力
    if len(cnt_list) == 0:
        print(0)
    else:
        print(max(cnt_list) + K)
