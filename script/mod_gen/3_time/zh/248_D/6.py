def find_num(arr,l,r,x):
    count = 0
    for i in range(l-1,r):
        if arr[i] == x:
            count += 1
    return count

if __name__ == '__main__':
    find_num()