def getPermutations(N, P):
    permutations = []
    for i in range(1, N+1):
        for j in range(1, N+1):
            if P[j-1] == i:
                permutations.append(j)
    return permutations

if __name__ == '__main__':
    getPermutations()