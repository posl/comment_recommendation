def calc_expectation(n, k, p):
    expectation = 0
    for i in range(k):
        expectation += (p[i] + 1) / 2
    max_expectation = expectation
    for i in range(k, n):
        expectation += (p[i] + 1) / 2
        expectation -= (p[i - k] + 1) / 2
        if expectation > max_expectation:
            max_expectation = expectation
    return max_expectation
n, k = map(int, input().split())
p = list(map(int, input().split()))
print(calc_expectation(n, k, p))

if __name__ == '__main__':
    calc_expectation()