def swap_list(list1, p, q, r, s):
    list2 = list1[p-1:q] + list1[r-1:s]
    list2.reverse()
    list1[p-1:q] = list2[0:q-p+1]
    list1[r-1:s] = list2[q-p+1:]
    return list1
