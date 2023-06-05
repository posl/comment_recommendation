def swap_list(list, p, q, r, s):
    # 交换A的P项到Q项和R项到S项得到序列B
    list[p:q], list[r:s] = list[r:s], list[p:q]
    return list
