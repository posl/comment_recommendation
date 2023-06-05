def find_subset(N, A):
    for i in range(N):
        for j in range(i+1, N):
            if (A[i] + A[j]) % 200 == 0:
                return True
    return False

if __name__ == '__main__':
    find_subset()