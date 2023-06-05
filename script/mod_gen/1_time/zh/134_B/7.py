def calc_min_checker(tree_num, distance):
    if tree_num < 2:
        return 1
    else:
        return 1 + (tree_num - 2 * distance - 1) // (2 * distance + 1)

if __name__ == '__main__':
    calc_min_checker()