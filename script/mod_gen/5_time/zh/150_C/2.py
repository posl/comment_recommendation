def permutation(n, p, q):
    p_rank = 0
    q_rank = 0
    for i in range(n):
        p_rank += p[i] * 10 ** (n - i - 1)
        q_rank += q[i] * 10 ** (n - i - 1)
    return p_rank, q_rank

if __name__ == '__main__':
    permutation()