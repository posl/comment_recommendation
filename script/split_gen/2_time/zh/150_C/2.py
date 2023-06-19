def permutation(n, p, q):
    count = 0
    for i in range(n):
        for j in range(n):
            if p[i] == q[j]:
                count += abs(i-j)
    return count
