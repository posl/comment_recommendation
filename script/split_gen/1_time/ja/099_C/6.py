def main():
    N = int(input())
    # 一回の操作で引き出せる金額のリスト
    # 1円, 6円, 6^2, 6^3, ..., 9円, 9^2, 9^3, ...
    money_list = [1]
    for i in range(1, 6):
        money_list.append(6 ** i)
    for i in range(1, 6):
        money_list.append(9 ** i)
    # 一回の操作で引き出せる金額のリストを降順にソート
    money_list.sort(reverse=True)
    # 一回の操作で引き出せる金額のリストを出力
    print(money_list)
    # 一回の操作で引き出せる金額のリストを用いて、
    # ちょうど N 円を引き出すのに必要な操作回数を求める
    count = 0
    for money in money_list:
        count += N // money
        N %= money
    # 一回の操作で引き出せる金額のリストを用いて、
    # ちょうど N 円を引き出すのに必要な操作回数を出力
    print(count)
