def main():
    h = list(map(int, input().strip().split()))
    w = list(map(int, input().strip().split()))
    # 3*3的矩阵，所以一共9个位置
    # 9个位置中，每个位置都有9种填法，但是有条件，所以减少一些
    # 1.每行的和都是固定的，那么就可以确定第一行的任意一个位置的数
    # 2.第一列的和也是固定的，那么就可以确定第一列的任意一个位置的数
    # 3.第二行的和也是固定的，那么就可以确定第二行的任意一个位置的数
    # 4.第二列的和也是固定的，那么就可以确定第二列的任意一个位置的数
    # 5.第三行的和也是固定的，那么就可以确定第三行的任意一个位置的数
    # 6.第三列的和也是固定的，那么就可以确定第三列的任意一个位置的数
    # 7.对角线的和也是固定的，那么就可以确定对角线的任意一个位置的数
    # 8.对角线的和也是固定的，那么就可以确定对角线的任意一个位置的数
    # 1.确定第一行的任意一个位置的数
    # 2.确定第一列的任意一个位置的数
    # 3.确定第二行的任意一个位置的数
    # 4.确定第二列的任意一个位置的数
    # 5.确定第三行的任意一个位置的数
    # 6.确定第三列的任意一个位置的数
    # 7.确定对角线的任意一个位置的数
    # 8.确定对角线的任意一个位置的数
    # 9.确定对角线的任意一个

if __name__ == '__main__':
    main()