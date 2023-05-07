def main():
    #入力
    L, R = map(int, input().split())
    S = input()
    #L-1文字目までとR文字目以降を別々に取得
    front = S[:L-1]
    back = S[R:]
    #L-1文字目からR文字目までを反転して取得
    middle = S[L-1:R][::-1]
    #結合して出力
    print(front + middle + back)
