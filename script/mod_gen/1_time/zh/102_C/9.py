def func(n, A):
    b = 0
    min = 0
    for i in range(n):
        min += abs(A[i] - (b + i + 1))
    return min

if __name__ == '__main__':
    func()