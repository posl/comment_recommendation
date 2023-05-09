def main():
    #入力
    A,B = map(int,input().split())
    #A+Bを計算
    C = A+B
    #A+Bを文字列に変換
    C = str(C)
    #Cの桁数を取得
    C_len = len(C)
    #Cの各桁の値を取得
    C_list = list(map(int,C))
    #繰り上がりフラグ
    flag = 0
    #Cの各桁の値が10以上の場合
    for i in range(C_len):
        if C_list[i] >= 10:
            flag = 1
            break
    #繰り上がりフラグにより出力
    if flag == 0:
        print("Easy")
    else:
        print("Hard")
