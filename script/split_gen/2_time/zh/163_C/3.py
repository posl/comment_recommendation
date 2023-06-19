def getSubordinateNums(a, n):
    # a: list of int
    # n: int
    # return: list of int
    # return the number of direct subordinates of each member
    # a[i] is the direct superior of i+1
    # a[0] is the direct superior of 1
    # a[1] is the direct superior of 2
    # a[n-1] is the direct superior of n
    # a[i] < i+1
    # a[0] = 1
    # a[i] = i+1 is not allowed
    # i+1 is the member id
    # a[i] is the direct superior of i+1
    # i+1 is the direct subordinate of a[i]
    # a[i] is the direct superior of i+1
    # i+1 is the direct subordinate of a[i]
    # a[i] is the direct superior of i+1
    # i+1 is the direct subordinate of a[i]
    # a[i] is the direct superior of i+1
    # i+1 is the direct subordinate of a[i]
    # a[i] is the direct superior of i+1
    # i+1 is the direct subordinate of a[i]
    # a[i] is the direct superior of i+1
    # i+1 is the direct subordinate of a[i]
    # a[i] is the direct superior of i+1
    # i+1 is the direct subordinate of a[i]
    # a[i] is the direct superior of i+1
    # i+1 is the direct subordinate of a[i]
    # a[i] is the direct superior of i+1
    # i+1 is the direct subordinate of a[i]
    # a[i] is the direct superior of i+1
    # i+1 is the direct subordinate of a[i]
    subNums = [0] * n
    for i in range(1, n):
        subNums[a[i]-1] += 1
    return subNums
