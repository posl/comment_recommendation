def main():
    # Read input
    N, M = map(int, input().split())
    A = []
    B = []
    C = []
    D = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for i in range(M):
        c, d = map(int, input().split())
        C.append(c)
        D.append(d)
    # Solve the problem
    # Create a list of all possible permutations of N elements
    import itertools
    perms = list(itertools.permutations(range(1,N+1)))
    # Create a list of all possible permutations of M elements
    import itertools
    permsM = list(itertools.permutations(range(0,M)))
    # Check whether the two toys have the same shape
    for perm in perms:
        for permM in permsM:
            # Check whether the two toys have the same shape
            # for a given permutation of N elements and a given permutation of M elements
            for i in range(M):
                if (A[permM[i]] == perm[C[i]-1] and B[permM[i]] == perm[D[i]-1]) or (A[permM[i]] == perm[D[i]-1] and B[permM[i]] == perm[C[i]-1]):
                    continue
                else:
                    break
            else:
                print("Yes")
                exit()
    print("No")
