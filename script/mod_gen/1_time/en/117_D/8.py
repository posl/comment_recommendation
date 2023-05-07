def solve(N, K, A):
    # 1. Find the maximum bit of K
    max_bit = 0
    for i in range(64):
        if K & (1 << i) == 0:
            break
        max_bit = i
    # 2. Find the maximum bit of A
    max_bit_A = 0
    for a in A:
        for i in range(64):
            if a & (1 << i) == 0:
                break
            max_bit_A = max(max_bit_A, i)
    # 3. Find the maximum value of f
    max_f = 0
    for i in range(max_bit_A, -1, -1):
        # 3.1. Find the maximum value of f when X has 1 in the i-th bit
        max_f_1 = max_f + (1 << i)
        # 3.2. Find the maximum value of f when X has 0 in the i-th bit
        max_f_0 = max_f
        for a in A:
            if a & (1 << i) != 0:
                max_f_0 += (1 << i)
        # 3.3. Update the maximum value of f
        if K & (1 << i) != 0 and max_f_0 < max_f_1:
            max_f = max_f_1
        else:
            max_f = max_f_0
    return max_f

if __name__ == '__main__':
    solve()