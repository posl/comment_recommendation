def solve(N, M, AB):
    # 2 <= N <= 2 * 10**5
    # 1 <= M <= 2 * 10**5
    # 1 <= A_i, B_i <= N
    # A_i != B_i
    # All values in input are integers.
    # Input is given from Standard Input in the following format:
    # N M
    # A_1 B_1
    # .
    # .
    # .
    # A_M B_M
    # Print the answer.
    # Among the sequences P that are permutations of (1, 2, ..., N) and satisfy the condition below, find the lexicographically smallest sequence.
    # For each i = 1, ..., M, A_i appears earlier than B_i in P.
    # If there is no such P, print -1.
    # 2 3
    # 1 2
    # 1 2
    # 2 1
    # -1
    # 4 3
    # 2 1
    # 3 4
    # 2 4
    # 2 1 3 4
    # The following five permutations P satisfy the condition: (2, 1, 3, 4), (2, 3, 1, 4), (2, 3, 4, 1), (3, 2, 1, 4), (3, 2, 4, 1). The lexicographically smallest among them is (2, 1, 3, 4).
    # 2 <= N <= 2 * 10**5
    # 1 <= M <= 2 * 10**5
    # 1 <= A_i, B_i <= N
    # A_i != B_i
    # All values in input are integers.
    # Input is given from Standard Input in the following format:
    # N M
    # A_1 B_1
    # .
    # .
    # .
    # A_M B_M
    # Print the answer.
    # Among the sequences P that are permutations of (1, 2, ..., N) and satisfy the condition below, find the lexicographically smallest sequence.
    # For each i = 1, ..., M

if __name__ == '__main__':
    solve()