def sum_of_subarrays(a):
    n = len(a)
    result = 0
    for i in range(n):
        for j in range(i, n):
            result += (j-i+1) * sum(a[i:j+1])
    return result

if __name__ == '__main__':
    sum_of_subarrays()