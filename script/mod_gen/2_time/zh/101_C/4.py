def get_min(A, K):
    min_num = 1000001
    for i in range(len(A)-K+1):
        min_num = min(A[i+K-1]-A[i], min_num)
    return min_num

if __name__ == '__main__':
    get_min()