def f(x, arr):
    sum = 0
    for i in range(len(arr)):
        sum += x ^ arr[i]
    return sum
