def main():
    # 入力
    N = int(input())
    # 処理
    ans = 1000 - N % 1000
    if ans == 1000:
        ans = 0
    # 出力
    print(ans)
