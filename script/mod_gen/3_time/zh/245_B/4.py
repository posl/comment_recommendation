def find_min_not_in_list(l):
    l.sort()
    i = 0
    for x in l:
        if x < 0:
            continue
        elif x == i:
            i += 1
        elif x > i:
            return i
    return i

if __name__ == '__main__':
    find_min_not_in_list()