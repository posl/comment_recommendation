def main():
    # 標準入力から A,B,Wを取得
    A,B,W = map(int,input().split())
    # Wをキログラムからグラムに変換
    W = W * 1000
    # 最小値と最大値を初期化
    min = 0
    max = 0
    # 最小値を求める
    if W % B == 0:
        min = int(W / B)
    else:
        min = int(W / B) + 1
    # 最大値を求める
    if W % A == 0:
        max = int(W / A)
    else:
        max = int(W / A) + 1
    # 最小値と最大値を出力
    if min <= max:
        print(min,max)
    else:
        print("UNSATISFIABLE")

if __name__ == '__main__':
    main()