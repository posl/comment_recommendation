def main():
    # 入力
    X, K = map(int, input().split())
    # 処理
    for i in range(K):
        X = round(X, -i)
    # 出力
    print(X)
