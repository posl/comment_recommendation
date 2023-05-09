def findCombinationsUtil(arr, index, num, reducedNum, A, B, N):
    # Base condition
    if (reducedNum < 0):
        return 0
    # If combination is
    # found, print it
    if (reducedNum == 0):
        #print(arr[:index])
        #print(A)
        #print(B)
        for i in range(index):
            for j in range(N):
                if A[j] == arr[i]:
                    if B[j] > 0:
                        B[j] -= 1
                    else:
                        return 0
        return 1
    # Find the previous number
    # stored in arr[]. It helps
    # in maintaining increasing
    # order
    prev = 1 if (index == 0) else arr[index - 1]
    # note loop starts from
    # previous number i.e. at
    # array location index - 1
    for k in range(prev, num + 1):
        # next element of
        # array is k
        arr[index] = k
        # call recursively with
        # reduced number
        if findCombinationsUtil(arr, index + 1, num, reducedNum - k, A, B, N) == 1:
            return 1
    return 0
