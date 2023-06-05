def get_binary_position_set(num):
    binary_position_set = []
    i = 0
    while num != 0:
        if num & 1 == 1:
            binary_position_set.append(i)
        num = num >> 1
        i += 1
    return binary_position_set

if __name__ == '__main__':
    get_binary_position_set()