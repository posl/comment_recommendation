def getKthNumber(k):
    k -= 1
    result = 0
    i = 0
    while k > 0:
        if k % 2 == 1:
            result += 2 * (10 ** i)
        k /= 2
        i += 1
    return result

if __name__ == '__main__':
    getKthNumber()