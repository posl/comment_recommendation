def make_yen_list():
    yen_list = [1]
    for i in range(1, 6):
        yen_list.append(6**i)
        yen_list.append(9**i)
    return yen_list

if __name__ == '__main__':
    make_yen_list()