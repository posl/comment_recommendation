def sum_of_products(arr):
    sum = 0
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            sum += arr[i]*arr[j]
    return sum

if __name__ == '__main__':
    sum_of_products()