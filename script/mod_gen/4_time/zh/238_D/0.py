def getBitSum(num):
    sum = 0
    while num != 0:
        sum += num & 1
        num = num >> 1
    return sum

if __name__ == '__main__':
    getBitSum()