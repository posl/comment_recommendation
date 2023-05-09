def main():
    N = int(input())
    A = list(map(int, input().split()))
    # Aに含まれない最小の正の整数を求める
    # Aに含まれる正の整数は0以上2000以下であることがわかる
    # 0以上2000以下の正の整数は2001個ある
    # これらのうちAに含まれるものを取り除き、残ったもののうち最小のものが答え
    # これをsetを使って実現する
    # まずAをsetに変換する
    # その後、setを使って0以上2000以下の正の整数を生成し、Aに含まれないものを取り除く
    # その後、setの中身をlistに変換し、sort関数でソートする
    # その後、listの先頭の要素が答え
    A_set = set(A)
    A_set = set(range(2001)) - A_set
    A_list = list(A_set)
    A_list.sort()
    print(A_list[0])
