def get_max_xor_sum(N, A):
    max_xor_sum = 0
    for i in range(N):
        for j in range(i+1, N):
            xor_sum = A[i] ^ A[j]
            if xor_sum > max_xor_sum:
                max_xor_sum = xor_sum
    return max_xor_sum

if __name__ == '__main__':
    get_max_xor_sum()