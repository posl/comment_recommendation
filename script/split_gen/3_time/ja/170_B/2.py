def main():
    # 入力
    X, Y = map(int, input().split())
    # 処理
    for i in range(X+1):
        if 2*i + 4*(X-i) == Y:
            # 出力
            print('Yes')
            return
    # 出力
    print('No')
