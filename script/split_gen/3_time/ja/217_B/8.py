def main():
    # 入力
    S = [input() for _ in range(3)]
    # 出力
    print('ABC' if 'ABC' not in S else 'ARC' if 'ARC' not in S else 'AGC' if 'AGC' not in S else 'AHC')
