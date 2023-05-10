def f(x, A):
    # x XOR A_1 + x XOR A_2 + ... + x XOR A_N
    # = (x XOR x XOR A_1) + (x XOR x XOR A_2) + ... + (x XOR x XOR A_N)
    # = (A_1) + (A_2) + ... + (A_N)
    # = A_1 + A_2 + ... + A_N
    return sum(A)
