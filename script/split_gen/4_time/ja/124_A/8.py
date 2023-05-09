def main():
    # 標準入力から A, B を取得する
    A, B = map(int, input().split())
    # ボタンを 2 回押す場合
    ans = max(A + A - 1, B + B - 1)
    # ボタンを 1 回ずつ押す場合
    ans = max(ans, A + B)
    # 結果を出力する
    print(ans)
