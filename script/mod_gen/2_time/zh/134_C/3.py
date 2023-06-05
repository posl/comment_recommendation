def calc_min_checker_num(num_of_trees, distance):
    return num_of_trees // (2 * distance + 1) + 1

if __name__ == '__main__':
    calc_min_checker_num()