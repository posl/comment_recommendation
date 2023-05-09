def main():
    #入力
    x, y = map(int, input().split())
    #計算
    ans = (y - x + 9) // 10
    #出力
    print(ans)
