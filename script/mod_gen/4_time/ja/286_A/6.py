def swap_list(list, p, q, r, s):
    list[p-1:q], list[r-1:s] = list[r-1:s], list[p-1:q]
    return list

if __name__ == '__main__':
    swap_list()