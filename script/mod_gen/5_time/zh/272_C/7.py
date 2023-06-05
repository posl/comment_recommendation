def findEvenSum(arr):
    evenList = []
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            evenList.append(i)
    if len(evenList) == 0:
        return -1
    else:
        evenSum = 0
        for i in range(len(evenList)):
            for j in range(i+1, len(evenList)):
                if arr[evenList[i]] + arr[evenList[j]] > evenSum:
                    evenSum = arr[evenList[i]] + arr[evenList[j]]
        return evenSum

if __name__ == '__main__':
    findEvenSum()