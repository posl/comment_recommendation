def main():
    #入力
    N, M = map(int, input().split())
    PY = [list(map(int, input().split())) for _ in range(M)]
    #県ごとに市をソート
    PY.sort(key=lambda x: x[0])
    #print(PY)
    #市ごとの認識番号を格納するリスト
    ans = [0] * M
    #県ごとに市の番号を振り分ける
    for i in range(M):
        if i == 0:
            #最初の市の場合
            ans[i] = str(PY[i][0]).zfill(6) + str(1).zfill(6)
            #print(ans[i])
        elif PY[i][0] != PY[i - 1][0]:
            #県が変わった場合
            ans[i] = str(PY[i][0]).zfill(6) + str(1).zfill(6)
            #print(ans[i])
        else:
            #県が変わらない場合
            ans[i] = str(PY[i][0]).zfill(6) + str(int(ans[i - 1][6:]) + 1).zfill(6)
            #print(ans[i])
    #出力
    for i in range(M):
        print(ans[i])
