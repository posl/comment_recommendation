def main():
    # 入力
    K = int(input())
    # 処理
    even = K//2
    odd = K//2 + K%2
    # 出力
    print(even*odd)
