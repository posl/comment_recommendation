def score(A):
    s = 0
    for i in range(Q):
        if A[b[i]-1] - A[a[i]-1] == c[i]:
            s += d[i]
    return s

if __name__ == '__main__':
    score()