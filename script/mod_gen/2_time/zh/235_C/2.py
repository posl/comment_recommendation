def get_index(num, k, list):
    count = 0
    for i in range(len(list)):
        if list[i] == num:
            count += 1
            if count == k:
                return i + 1
    return -1

if __name__ == '__main__':
    get_index()