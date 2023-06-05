def get_num_of_covering_rectangles(h, w, a, b):
    if h == 1 and w == 1:
        return 1
    elif h == 1 and w == 2:
        return 1
    elif h == 2 and w == 1:
        return 1
    elif h == 2 and w == 2:
        return 2
    elif h == 1:
        return get_num_of_covering_rectangles(1, w-1, a, b-1)
    elif w == 1:
        return get_num_of_covering_rectangles(h-1, 1, a-1, b)
    elif h == 2:
        return get_num_of_covering_rectangles(2, w-1, a, b-1) + get_num_of_covering_rectangles(1, w-1, a, b-1)
    elif w == 2:
        return get_num_of_covering_rectangles(h-1, 2, a-1, b) + get_num_of_covering_rectangles(h-1, 1, a-1, b)
    else:
        return get_num_of_covering_rectangles(h-1, w, a-1, b) + get_num_of_covering_rectangles(h, w-1, a, b-1)
