def check_consecutive(arr, n):
    for i in range(n-1):
        if arr[i] == arr[i+1]:
            return True
    return False

if __name__ == '__main__':
    check_consecutive()