def find_min_int_not_in_list(list):
    list.sort()
    min = 0
    for i in list:
        if i == min:
            min += 1
    return min

if __name__ == '__main__':
    find_min_int_not_in_list()