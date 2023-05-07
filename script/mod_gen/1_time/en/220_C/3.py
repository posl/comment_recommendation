def solve(N, A, X):
    B = A * 100000
    sum = 0
    for i in range(1000000):
        sum += B[i]
        if sum > X:
            return i + 1
    return 0

if __name__ == '__main__':
    solve()