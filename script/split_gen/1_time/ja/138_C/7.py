def main():
    # 入力
    N = int(input())
    v = list(map(int, input().split()))
    # 結果出力
    print(sum(v) / N)
