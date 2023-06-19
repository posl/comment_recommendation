def get_median(arr):
    arr.sort()
    return arr[len(arr)//2+1]

if __name__ == '__main__':
    get_median()