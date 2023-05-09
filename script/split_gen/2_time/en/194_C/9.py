def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    # 1. sum_{i = 2}^{N} sum_{j = 1}^{i - 1} (A_i - A_j)^2
    # 2. sum_{i = 2}^{N} sum_{j = 1}^{i - 1} (A_i^2 - 2A_iA_j + A_j^2)
    # 3. sum_{i = 2}^{N} sum_{j = 1}^{i - 1} (A_i^2 - 2A_iA_j + A_j^2) = sum_{i = 2}^{N} A_i^2 - 2sum_{i = 2}^{N} A_iA_j + sum_{i = 2}^{N} sum_{j = 1}^{i - 1} A_j^2
    # 4. sum_{i = 2}^{N} A_i^2 - 2sum_{i = 2}^{N} A_iA_j + sum_{i = 2}^{N} sum_{j = 1}^{i - 1} A_j^2 = sum_{i = 2}^{N} A_i^2 - 2sum_{i = 2}^{N} A_iA_j + sum_{i = 2}^{N} sum_{j = 1}^{i - 1} A_j^2 = sum_{i = 2}^{N} A_i^2 - 2sum_{i = 2}^{N} A_iA_j + sum_{i = 2}^{N} sum_{j = 1}^{i - 1} A_j^2 = sum_{i = 2}^{N} A_i^2 - 2sum_{i = 2}^{N} A_iA_j + sum_{i = 2}^{N} sum_{j = 1}^{i - 1} A_j^2 = sum_{i = 2}^{N} A_i^2 - 2sum_{i = 2}^{N} A_iA_j + sum_{i =
