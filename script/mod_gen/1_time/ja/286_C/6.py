def main():
    N, A, B = map(int, input().split())
    S = input()
    #S = "rrefa"
    #A = 1
    #B = 2
    #S = "bcdfcgaa"
    #A = 10**9
    #B = 10**9
    #文字列が回文かどうか判定する関数
    def is_palindrome(s):
        return s == s[::-1]
    #文字列を左に1つずつずらす関数
    def shift(s):
        return s[1:] + s[0]
    #文字列を回文にするために必要なコストを計算する関数
    def cost(s):
        #文字列が回文なら0を返す
        if is_palindrome(s):
            return 0
        #文字列の左端と右端が同じなら文字列を左に1つずつずらして再帰的にコストを計算する
        if s[0] == s[-1]:
            return cost(s[1:-1])
        #文字列の左端と右端が異なるなら文字列を左に1つずつずらして再帰的にコストを計算し、その結果にBを足す
        else:
            return cost(s[1:-1]) + B
    #文字列を回文にするために必要なコストを計算する
    c = cost(S)
    #文字列を回文にするために必要なコストがAより小さいならAを出力する
    if c < A:
        print(A)
    #文字列を回文にするために必要なコストがAより大きいなら文字列を左に1つずつずらして回文になるまで繰り返す
    else:
        #文字列を回文にするために必要なコストを計算する
        c = cost(S)
        #文字列を回文にするために必要なコストがA

if __name__ == '__main__':
    main()