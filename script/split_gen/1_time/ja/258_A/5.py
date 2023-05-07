def main():
    #入力
    K = int(input())
    #時刻を計算
    HH = 21 + K // 60
    MM = K % 60
    #出力
    print(str(HH) + ":" + str(MM))
