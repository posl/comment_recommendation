def swap_list(l, p, q, r, s):
    new_list = []
    new_list.extend(l[0:p])
    new_list.extend(l[r:s+1])
    new_list.extend(l[q:r])
    new_list.extend(l[p:q])
    new_list.extend(l[s+1:])
    return new_list
