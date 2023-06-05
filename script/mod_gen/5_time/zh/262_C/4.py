def findMin(a, i):
    mini = a[i]
    minIndex = i
    for j in range(i+1, len(a)):
        if a[j] < mini:
            mini = a[j]
            minIndex = j
    return minIndex

if __name__ == '__main__':
    findMin()