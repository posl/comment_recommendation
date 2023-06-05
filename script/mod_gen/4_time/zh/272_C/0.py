def check_even_sum(A):
    A = sorted(A)
    max_even = -1
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if (A[i] + A[j]) % 2 == 0:
                max_even = max(max_even, A[i] + A[j])
    return max_even

if __name__ == '__main__':
    check_even_sum()