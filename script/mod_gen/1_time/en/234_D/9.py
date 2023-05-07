def get_kth_value(arr, k):
    arr.sort(reverse=True)
    return arr[k-1]

if __name__ == '__main__':
    get_kth_value()