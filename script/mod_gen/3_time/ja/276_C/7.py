def next_permutation(perm):
    N = len(perm)
    # 1. Find the largest x such that P[x] < P[x+1].
    x = -1
    for i in range(N-1):
        if perm[i] < perm[i+1]:
            x = i
    if x == -1:
        return False
    # 2. Find the largest y such that P[x] < P[y].
    y = -1
    for i in range(x+1, N):
        if perm[x] < perm[i]:
            y = i
    # 3. Swap P[x] and P[y].
    perm[x], perm[y] = perm[y], perm[x]
    # 4. Reverse P[x+1 .. N].
    perm[x+1:] = reversed(perm[x+1:])
    return True

if __name__ == '__main__':
    next_permutation()