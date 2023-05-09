def swapper(list, p, q, r, s):
    p = p - 1
    q = q - 1
    r = r - 1
    s = s - 1
    for i in range(q - p + 1):
        list[p + i], list[s - i] = list[s - i], list[p + i]
    return list

if __name__ == '__main__':
    swapper()