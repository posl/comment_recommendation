def main():
    # Get input
    s, k = input().split()
    # Get permutations
    s = list(s)
    k = int(k)
    perms = []
    get_permutations(s, 0, len(s) - 1, perms)
    # Sort
    perms.sort()
    # Print the k-th permutation
    print(perms[k - 1])
