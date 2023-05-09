def main():
    #入力
    a, b, c, d, e = map(int, input().split())
    #出力
    print(len(set([a, b, c, d, e])))
