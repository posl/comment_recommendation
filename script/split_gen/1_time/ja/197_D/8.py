def main():
    #入力
    N = int(input())
    x_0, y_0 = map(int, input().split())
    x_N_2, y_N_2 = map(int, input().split())
    #処理
    x_1 = x_0 + (x_N_2 - x_0) * (N / 4) / (N / 2)
    y_1 = y_0 + (y_N_2 - y_0) * (N / 4) / (N / 2)
    #出力
    print(x_1, y_1)
