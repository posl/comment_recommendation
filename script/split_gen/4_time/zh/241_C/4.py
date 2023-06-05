def checkRow(arr,row):
    for i in range(0, len(arr[row])):
        if arr[row][i] == '#':
            return False
    return True
