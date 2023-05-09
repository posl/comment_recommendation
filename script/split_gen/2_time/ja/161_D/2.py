def main():
    #入力
    K = int(input())
    #ルンルン数を格納するリスト
    L = [1,2,3,4,5,6,7,8,9]
    #ルンルン数を格納するリストにルンルン数を追加していく
    for i in range(10**5):
        s = str(L[i])
        #ルンルン数の末尾の数字
        last = int(s[-1])
        #ルンルン数の末尾の数字が9の場合
        if last == 9:
            L.append(int(s+str(last-1)))
        #ルンルン数の末尾の数字が0の場合
        elif last == 0:
            L.append(int(s+str(last+1)))
        #ルンルン数の末尾の数字が1~8の場合
        else:
            L.append(int(s+str(last-1)))
            L.append(int(s+str(last+1)))
    #出力
    print(L[K-1])
