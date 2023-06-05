def get_max_value(vlist):
    vlist.sort()
    while len(vlist) > 1:
        vlist.append((vlist.pop(0) + vlist.pop(0)) / 2)
    return vlist[0]

if __name__ == '__main__':
    get_max_value()