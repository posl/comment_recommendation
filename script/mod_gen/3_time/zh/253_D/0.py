def getSum(N, a, b):
    sum = 0
    for i in range(1, N + 1):
        if i % a != 0 and i % b != 0:
            sum += i
    return sum

if __name__ == '__main__':
    getSum()