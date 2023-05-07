def main():
    S = input()
    N = len(S)
    # 0を黒, 1を白とする
    # 0を黒にしたときの最小塗り替え回数
    count0 = 0
    # 1を白にしたときの最小塗り替え回数
    count1 = 0
    # 0を黒にしたときの前のタイルの色
    prev0 = 0
    # 1を白にしたときの前のタイルの色
    prev1 = 1
    for i in range(N):
        if S[i] == '0':
            if prev0 == 0:
                count0 += 1
                prev0 = 1
            else:
                prev0 = 0
        else:
            if prev0 == 1:
                count0 += 1
                prev0 = 0
            else:
                prev0 = 1
        if S[i] == '1':
            if prev1 == 0:
                count1 += 1
                prev1 = 1
            else:
                prev1 = 0
        else:
            if prev1 == 1:
                count1 += 1
                prev1 = 0
            else:
                prev1 = 1
    print(min(count0, count1))
