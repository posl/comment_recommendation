def main():
    #入力
    n = input()
    #計算
    n = n.replace("1", "x")
    n = n.replace("9", "1")
    n = n.replace("x", "9")
    #出力
    print(n)
