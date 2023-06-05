def count_pairs(A):
    count = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if (A[i] - A[j]) % 200 == 0:
                count += 1
    return count
