def getLuckyNumber(k):
    count = 0
    num = 1
    while count < k:
        if isLucky(num):
            count += 1
        num += 1
    return num - 1

if __name__ == '__main__':
    getLuckyNumber()