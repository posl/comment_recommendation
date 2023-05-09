def check_even_pair(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if (array[i] + array[j]) % 2 == 0:
                return array[i] + array[j]
    return -1

if __name__ == '__main__':
    check_even_pair()