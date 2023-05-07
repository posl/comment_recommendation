def main():
    # 標準入力から1行取得
    # 1行目の入力値をスペースで分割して、リストに変換
    # map()関数で、リストの各要素をint型に変換
    m, h = map(int, input().split())
    # hをmで割った余りが0ならYes、そうでなければNoを出力
    print("Yes" if h % m == 0 else "No")
