def main():
    #入力
    X, Y = map(int, input().split())
    #足の本数の差を計算
    diff = Y - 2 * X
    #亀の数を計算
    turtle = diff // 2
    #鶴の数を計算
    crane = X - turtle
    #亀と鶴の数が正しいか判定
    if turtle >= 0 and crane >= 0 and 4 * turtle + 2 * crane == Y:
        print("Yes")
    else:
        print("No")
