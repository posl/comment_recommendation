def main():
    K = int(input())
    #K = 63
    #K = 45
    #K = 100
    #21時ちょうどを基準にする
    HH = 21
    MM = 0
    #K分後の時間を計算する
    MM += K
    #MMが60以上になったら、HHを1増やし、MMを60から引く
    while MM >= 60:
        HH += 1
        MM -= 60
    #HHが24以上になったら、HHを24から引く
    while HH >= 24:
        HH -= 24
    #HHが1桁の場合、先頭に0を付ける
    if HH < 10:
        HH = "0" + str(HH)
    #MMが1桁の場合、先頭に0を付ける
    if MM < 10:
        MM = "0" + str(MM)
    print(str(HH) + ":" + str(MM))
