def find_median(array):
    array.sort()
    return array[(len(array)-1)//2]

if __name__ == '__main__':
    find_median()