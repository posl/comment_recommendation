def lexico_smallest_permutation(n, p):
    p = p.split()
    p = list(map(int, p))
    q = []
    for i in range(n):
        q.append(p.index(i+1)+1)
    q = list(map(str, q))
    return ' '.join(q)
