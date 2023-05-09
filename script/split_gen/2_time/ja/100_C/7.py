def main():
    # 標準入力から N と a を取得する
    N = int(input())
    a = list(map(int, input().split()))
    # 操作回数をカウントする変数
    count = 0
    # a の各要素に対して操作を行う
    for i in range(N):
        # a[i] が 2 で割り切れる間は 2 で割り続ける
        while a[i] % 2 == 0:
            a[i] = a[i] / 2
            count += 1
    # 操作回数を出力する
    print(count)
