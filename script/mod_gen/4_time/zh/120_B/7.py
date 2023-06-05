def getDivisor(a, b):
    divisor = []
    for i in range(1, min(a, b)+1):
        if a % i == 0 and b % i == 0:
            divisor.append(i)
    return divisor

if __name__ == '__main__':
    getDivisor()