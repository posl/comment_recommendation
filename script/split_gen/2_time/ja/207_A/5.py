def main():
    # A B Cを入力
    A, B, C = map(int, input().split())
    # AとBの合計値とAとCの合計値を比較し、大きい方の値を出力
    print(max(A + B, B + C, C + A))
