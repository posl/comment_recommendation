def swap_char(string, a, b):
    # print(string, a, b)
    l = list(string)
    l[a-1], l[b-1] = l[b-1], l[a-1]
    return "".join(l)
