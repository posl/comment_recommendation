def harvest_fruits(N, A):
    sum = 0
    for i in range(N):
        if A[i] > 10:
            sum += A[i] - 10
    return sum

if __name__ == '__main__':
    harvest_fruits()