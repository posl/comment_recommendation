def main():
    # データ入力
    a,b,c,d,e = map(int,input().split())
    # データ処理
    if a == b and b == c and d == e:
        print("Yes")
    elif a == b and c == d and d == e:
        print("Yes")
    else:
        print("No")
    # 出力
