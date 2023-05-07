def main():
    #入力
    abc = input()
    #abcが3桁の整数かどうか
    if len(abc) != 3:
        return -1
    #abcが0でない整数かどうか
    if int(abc) == 0:
        return -1
    #abcを各桁に分ける
    a = int(abc[0])
    b = int(abc[1])
    c = int(abc[2])
    #出力
    print(a+b+c + b+c+a + c+a+b)
