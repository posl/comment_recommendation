def swap_list(list, p, q, r, s):
    tmp = list[p-1:q]
    list[p-1:q] = list[r-1:s]
    list[r-1:s] = tmp
    return list
