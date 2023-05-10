def main():
    #1行目の入力を取得
    a,b = map(int,input().split())
    #A+Bが16以下かどうか
    if a+b <= 16:
        print("Yay!")
    else:
        print(":(")
