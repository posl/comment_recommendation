def get_count_of_triplets(A):
    N = len(A)
    count = 0
    for i in range(0, N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if A[i] != A[j] and A[j] != A[k] and A[i] != A[k]:
                    count += 1
    return count

if __name__ == '__main__':
    get_count_of_triplets()