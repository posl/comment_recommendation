def permutation(N, P):
    P = list(P)
    perm = []
    for i in range(N):
        for j in range(N):
            if j not in perm:
                perm.append(j)
                break
    return perm

if __name__ == '__main__':
    permutation()