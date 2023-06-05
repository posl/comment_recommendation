def find_nearest(array, value):
    if value < array[0]:
        return array[0]
    elif value > array[len(array)-1]:
        return array[len(array)-1]
    else:
        for i in range(len(array)):
            if array[i] >= value:
                if array[i] - value > value - array[i-1]:
                    return array[i-1]
                else:
                    return array[i]

if __name__ == '__main__':
    find_nearest()