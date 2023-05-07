def main():
    #入力
    abc = int(input())
    #abcを桁ごとに分割
    a = abc // 100
    b = abc % 100 // 10
    c = abc % 100 % 10
    #出力
    print(a+b+c+b+c+a+c+a+b)
