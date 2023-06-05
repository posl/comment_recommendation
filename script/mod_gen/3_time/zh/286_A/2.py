def reverse(arr,start,end):
    while start < end:
        arr[start],arr[end] = arr[end],arr[start]
        start += 1
        end -= 1
    return arr

if __name__ == '__main__':
    reverse()