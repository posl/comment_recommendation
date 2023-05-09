def main():
    # データ入力
    a, b, c = map(int, input().split())
    # 計算
    ans = a + b + c
    ans = max(ans, a + b * c)
    ans = max(ans, a * b + c)
    ans = max(ans, a * b * c)
    ans = max(ans, a * (b + c))
    ans = max(ans, (a + b) * c)
    # 結果出力
    print(ans)
