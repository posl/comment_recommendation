def main():
    S = input()
    # 0の数と1の数をカウント
    # 0の数と1の数の小さい方が答え
    print(min(S.count('0'), S.count('1')) * 2)
