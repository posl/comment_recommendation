def find_kth_min_num(list_num, k):
    list_num.sort()
    return list_num[k-1]

if __name__ == '__main__':
    find_kth_min_num()