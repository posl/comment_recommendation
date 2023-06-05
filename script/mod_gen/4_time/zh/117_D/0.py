def solve(N, K, A):
    # 二分探索
    # 0 <= X <= K
    # f(X) = (X XOR A_1) + (X XOR A_2) + ... + (X XOR A_N)
    # f(X) = (X XOR (A_1 + A_2 + ... + A_N)) + A_1 + A_2 + ... + A_N
    # f(X) = (X XOR S) + S
    # f(X) = X + S - 2 * (X AND S)
    # f(X) = (1 - 2) * (X AND S) + S
    # f(X) = -2 * (X AN

if __name__ == '__main__':
    solve()