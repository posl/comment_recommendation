def sum_of_squared_differences(N, A):
    sum = 0
    for i in range(1,N):
        for j in range(i):
            sum += (A[i] - A[j]) ** 2
    return sum

if __name__ == '__main__':
    sum_of_squared_differences()