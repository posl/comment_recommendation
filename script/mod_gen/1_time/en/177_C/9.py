def solve():
    N = int(input())
    A = [int(x) for x in input().split()]
    # (A_1 + A_2 + ... + A_N) ^ 2 - (A_1^2 + A_2^2 + ... + A_N^2)
    # = 2 * (A_1A_2 + A_1A_3 + ... + A_1A_N + A_2A_3 + ... + A_{N-1}A_N)
    # = 2 * (A_1A_2 + A_1A_3 + ... + A_1A_N + A_2A_3 + ... + A_{N-1}A_N)
    # = 2 * sum_{i=1}^{N-1}sum_{j=i+1}^{N} A_i A_j
    # = 2 * sum_{i=1}^{N}sum_{j=i+1}^{N} A_i A_j
    # = 2 * sum_{i=1}^{N} A_i * sum_{j=i+1}^{N} A_j
    # = 2 * sum_{i=1}^{N} A_i * (sum_{j=1}^{N} A_j - A_i)
    # = 2 * sum_{i=1}^{N} A_i * (sum_{j=1}^{N} A_j - A_i)
    # = 2 * sum_{i=1}^{N} A_i * (sum_{j=1}^{N} A_j - A_i)
    # = 2 * sum_{i=1}^{N} A_i * (sum_{j=1}^{N} A_j - A_i)
    # = 2 * sum_{i=1}^{N} A_i * (sum_{j=1}^{N} A_j - A_i)
    # = 2 * sum_{i=1}^{N} A_i * (sum_{j=1}^{N} A_j - A_i)
    # = 2 * sum_{i=1}^{N} A_i * (sum_{j=1}^{N} A_j - A_i)
    # = 2 * sum_{i=1}^{

if __name__ == '__main__':
    solve()