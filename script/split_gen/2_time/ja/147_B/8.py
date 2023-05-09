def main():
    #入力
    s = input()
    #回文にする必要がない場合
    if s == s[::-1]:
        #出力
        print(0)
        return
    #回文にする必要がある場合
    else:
        #回文にするためのハグの最小回数
        min_count = 0
        #文字列の長さ
        length = len(s)
        #文字列の長さの半分
        half_length = length // 2
        #文字列の長さが奇数の場合
        if length % 2 != 0:
            #文字列の半分の文字列を比較
            for i in range(half_length):
                #文字列の半分の文字列が異なる場合
                if s[i] != s[-(i+1)]:
                    #回文にするためのハグの最小回数を1増やす
                    min_count += 1
            #出力
            print(min_count)
            return
        #文字列の長さが偶数の場合
        else:
            #文字列の半分の文字列を比較
            for i in range(half_length):
                #文字列の半分の文字列が異なる場合
                if s[i] != s[-(i+1)]:
                    #回文にするためのハグの最小回数を1増やす
                    min_count += 1
            #出力
            print(min_count)
            return
