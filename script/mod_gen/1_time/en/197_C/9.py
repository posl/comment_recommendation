def solve(N, A):
    # 1. find the largest bit that is different
    # 2. divide into two groups
    # 3. the answer is the xor of the two groups
    max_bit = 0
    for i in range(N):
        for j in range(i+1, N):
            if A[i] != A[j]:
                max_bit = max(max_bit, A[i] ^ A[j])
    max_bit = max_bit.bit_length()
    #print(max_bit)
    if max_bit == 0:
        return 0
    else:
        max_bit -= 1
        #print(max_bit)
    group1 = 0
    group2 = 0
    for i in range(N):
        if A[i] & (1 << max_bit):
            group1 |= A[i]
        else:
            group2 |= A[i]
    return group1 ^ group2

if __name__ == '__main__':
    solve()