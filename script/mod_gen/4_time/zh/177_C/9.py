def sum_of_pairs(N,A):
    sum = 0
    for i in range(N-1):
        for j in range(i+1,N):
            sum += A[i]*A[j]
    return sum

if __name__ == '__main__':
    sum_of_pairs()