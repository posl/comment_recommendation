def swap(array, start, end):
    for i in range(start, end):
        array[i], array[i + 1] = array[i + 1], array[i]

if __name__ == '__main__':
    swap()