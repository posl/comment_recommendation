def main():
    N = int(input())
    s = [input() for _ in range(N)]
    # s.sort()  # この場合、s.sort()を実行すると実行時間が長くなる
    # これは、s.sort()を実行すると、sの中身が並び替えられてしまうため。
    # なので、sの中身を並び替えずに、s.sort()の結果を別の変数に格納する。
    s_sort = sorted(s)
    # print(s)
    # print(s_sort)
    # print(s_sort[0])
    # print(s_sort[1])
    # print(s_sort[2])
    # print(s_sort[3])
    # print(s_sort[4])
    # print(s_sort[0][0])
    # print(s_sort[0][1])
    # print(s_sort[0][2])
    # print(s_sort[0][3])
    # print(s_sort[0][4])
    # print(s_sort[0][5])
    # print(s_sort[0][6])
    # print(s_sort[0][7])
    # print(s_sort[0][8])
    # print(s_sort[0][9])
    # print(s_sort[1][0])
    # print(s_sort[1][1])
    # print(s_sort[1][2])
    # print(s_sort[1][3])
    # print(s_sort[1][4])
    # print(s_sort[1][5])
    # print(s_sort[1][6])
    # print(s_sort[1][7])
    # print(s_sort[1][8])
    # print(s_sort[1][9])
    # print(s_sort[2][0])
    # print(s_sort[2][1])
    # print(s_sort[2][2])
    # print(s_sort[2][3])
    # print(s_sort[2][4])
    # print(s_sort[2][5])
    # print(s_sort[2][6])
    # print(s_sort[2][7])
    # print(s_sort[2][8])
    # print(s_sort[2][9])
    # print(s_sort[3][0])