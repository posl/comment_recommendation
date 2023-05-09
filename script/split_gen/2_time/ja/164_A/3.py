def main():
    # 入力
    S, W = map(int, input().split())
    # 出力
    if S <= W:
        print("unsafe")
    else:
        print("safe")
