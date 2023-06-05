def countSnukes(n, k, d, A):
    snukes = [0 for i in range(n)]
    for i in range(k):
        for j in range(d[i]):
            snukes[A[i][j] - 1] += 1
    return snukes.count(0)

if __name__ == '__main__':
    countSnukes()