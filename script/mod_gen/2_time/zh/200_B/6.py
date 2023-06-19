def calculate(N, K):
    if K == 0:
        return N
    if N % 200 == 0:
        return calculate(N // 200, K - 1)
    else:
        return calculate(N * 1000 + 200, K - 1)

if __name__ == '__main__':
    calculate()