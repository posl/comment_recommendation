def swap_list(a, b, list):
    list[a:b], list[b:a] = list[b:a], list[a:b]
    return list
