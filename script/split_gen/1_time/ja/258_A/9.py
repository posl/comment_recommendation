def main():
    #入力
    K = int(input())
    #処理
    #21時からK分後の時刻を求める
    #HH:MMの形式で出力
    #HHは24時間制での時間を、MMは分を表す
    #時間または分が1桁のときは、先頭に0を追加して2桁の整数として表す
    #HH = 21 + K // 60
    #MM = (K % 60)
    HH = 21 + (K // 60)
    MM = (K % 60)
    if HH >= 24:
        HH = HH - 24
    if HH < 10:
        HH = '0' + str(HH)
    if MM < 10:
        MM = '0' + str(MM)
    print(str(HH) + ':' + str(MM))
