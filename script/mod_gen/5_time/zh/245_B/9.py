def find_min_num_not_in_list(list):
    min = 0
    for i in range(0, len(list)):
        if list[i] > min:
            break
        elif list[i] == min:
            min += 1
    return min

if __name__ == '__main__':
    find_min_num_not_in_list()