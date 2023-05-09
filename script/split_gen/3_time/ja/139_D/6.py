def main():
    # 入力
    N = int(input())
    # 出力
    if N % 2 == 0:
        print(N * (N // 2) - N // 2)
    else:
        print(N * (N // 2))
