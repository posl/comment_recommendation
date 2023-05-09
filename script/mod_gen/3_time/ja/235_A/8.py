def main():
    # 3つの数字を入力
    abc = input()
    # 3つの数字をリストに格納
    abc_list = list(abc)
    # 3つの数字をリストに格納
    bca_list = abc_list[1:] + abc_list[:1]
    # 3つの数字をリストに格納
    cab_list = abc_list[2:] + abc_list[:2]
    # 3つの数字をリストに格納
    xyz_list = [abc, ''.join(bca_list), ''.join(cab_list)]
    # 3つの数字をリストに格納
    xyz = int(''.join(xyz_list))
    # 3つの数字をリストに格納
    print(xyz)

if __name__ == '__main__':
    main()