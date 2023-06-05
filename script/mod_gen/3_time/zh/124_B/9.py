def get_max_index(list):
    max = list[0]
    index = 0
    for i in range(0, len(list)):
        if list[i] > max:
            max = list[i]
            index = i
    return index

if __name__ == '__main__':
    get_max_index()