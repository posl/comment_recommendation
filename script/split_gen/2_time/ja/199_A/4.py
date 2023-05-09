def main():
    #入力
    A, B, C = map(int, input().split())
    #A^2 + B^2 < C^2 なら Yes を、そうでないなら No を出力せよ。  
    if A ** 2 + B ** 2 < C ** 2:
        print("Yes")
    else:
        print("No")
