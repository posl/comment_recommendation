def findMinPositiveIntegerNotInArray(array):
    array.sort()
    min = 0
    for i in range(len(array)):
        if array[i] <= min:
            continue
        elif array[i] == min + 1:
            min = array[i]
        else:
            break
    return min + 1

if __name__ == '__main__':
    findMinPositiveIntegerNotInArray()