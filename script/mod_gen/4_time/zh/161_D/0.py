def get_num(k):
    list = []
    i = 1
    while True:
        if i % 10 == 0:
            i += 1
            continue
        list.append(i)
        i += 1
        if len(list) == k:
            break
    return list[-1]

if __name__ == '__main__':
    get_num()