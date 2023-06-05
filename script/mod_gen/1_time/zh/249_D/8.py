def count_pairs(A):
    N = len(A)
    counter = {}
    for i in range(N):
        if A[i] in counter:
            counter[A[i]] += 1
        else:
            counter[A[i]] = 1
    return counter

if __name__ == '__main__':
    count_pairs()