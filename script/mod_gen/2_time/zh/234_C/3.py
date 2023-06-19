def findKthNumber(k):
    if k <= 0:
        return -1
    result = 0
    while k > 0:
        result = result * 10 + 2
        k -= 1
    return result

if __name__ == '__main__':
    findKthNumber()