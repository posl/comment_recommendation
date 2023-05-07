def main():
    # 入力
    S = input()
    # 0と1の数を数える
    S0 = S.count('0')
    S1 = S.count('1')
    # 出力
    print(min(S0, S1))
