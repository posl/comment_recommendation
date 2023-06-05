def find_median(arr):
    arr.sort()
    return arr[int(len(arr)/2)]

if __name__ == '__main__':
    find_median()