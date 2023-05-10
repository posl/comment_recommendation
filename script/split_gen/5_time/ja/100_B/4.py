def main():
    # 標準入力から2行取得
    line1 = input()
    line2 = input()
    # 1行目をスペースで分割し、int型に変換して変数に格納
    line1_split = line1.split(" ")
    D = int(line1_split[0])
    N = int(line1_split[1])
    # 2行目をスペースで分割し、int型に変換して変数に格納
    line2_split = line2.split(" ")
    a = int(line2_split[0])
    b = int(line2_split[1])
    # 100で割り切れる場合は100に変換
    if a == 100:
        a = 101
    # 100で割り切れる場合は100に変換
    if b == 100:
        b = 101
    # Dが0の場合はaをN回繰り返す
    if D == 0:
        print(a*N)
    # Dが1の場合はaをN回繰り返し、100倍する
    elif D == 1:
        print(a*N*100)
    # Dが2の場合はaをN回繰り返し、10000倍する
    else:
        print(a*N*10000)
