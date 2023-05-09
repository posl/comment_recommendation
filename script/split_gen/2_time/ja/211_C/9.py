def main():
    S = input()
    #文字列Sの長さ
    N = len(S)
    #Sの中にある文字列の個数
    count = [0] * 26
    #文字列の個数を数える
    for i in range(N):
        count[ord(S[i]) - ord('a')] += 1
    #c,h,o,k,u,d,a,iの数
    c = count[2]
    h = count[7]
    o = count[14]
    k = count[10]
    u = count[20]
    d = count[3]
    a = count[0]
    i = count[8]
    #c,h,o,k,u,d,a,iの文字列の個数の総和
    sum = c + h + o + k + u + d + a + i
    #c,h,o,k,u,d,a,iの文字列の個数の総和が8より小さい場合
    if sum < 8:
        print(0)
    #c,h,o,k,u,d,a,iの文字列の個数の総和が8以上の場合
    else:
        #c,h,o,k,u,d,a,iの文字列の個数の総和から8を引いた数を計算
        sum = sum - 8
        #c,h,o,k,u,d,a,iの文字列の個数の総和から8を引いた数の階乗を計算
        for i in range(1, sum + 1):
            sum = sum * i
        #c,h,o,k,u,d,a,iの文字列の個数の総和から8を引いた数の階乗を計算
        for i in range(1, 8 + 1):
            sum = sum // i
        #c,h,o,k,u,d,a,iの文字列の個数の総和から8を引いた数の階乗を計算
        for i in range(1, 8 + 1):
            sum = sum // i
        #c,h,o,k,u,d,a,iの文字列
