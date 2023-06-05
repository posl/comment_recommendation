def find_seq(n, A):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if (A[i] + A[j]) % 200 == 0:
                return [i + 1], [j + 1]
    return [], []

if __name__ == '__main__':
    find_seq()