def count_subordinates(n, A):
    subordinates = [0] * n
    for i in range(1, n):
        subordinates[A[i-1]-1] += 1
    return subordinates

if __name__ == '__main__':
    count_subordinates()