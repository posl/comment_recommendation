def print_count_of_bottoms(s):
    # 记录连续的v的个数
    count_of_v = 0
    # 记录底的个数
    count_of_bottoms = 0
    for c in s:
        if c == 'v':
            count_of_v += 1
        else:
            count_of_bottoms += count_of_v
    print(count_of_bottoms)

if __name__ == '__main__':
    print_count_of_bottoms()