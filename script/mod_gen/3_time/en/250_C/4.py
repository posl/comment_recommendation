def swap(array, index):
    tmp = array[index]
    array[index] = array[index+1]
    array[index+1] = tmp

if __name__ == '__main__':
    swap()