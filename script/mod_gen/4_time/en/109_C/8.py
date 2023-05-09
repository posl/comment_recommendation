def calculate(N, X, x):
    result = 0
    for i in range(N):
        result = gcd(result, abs(X - x[i]))
    return result

if __name__ == '__main__':
    calculate()