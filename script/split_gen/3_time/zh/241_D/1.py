def get_min_k(list, k):
    list.sort(reverse=True)
    return list[k-1]
