def findMaxNum(n, m, a):
    # 用来组成数字1，2，3，4，5，6，7，8，9的火柴棒数量应该分别为2，5，5，4，5，6，3，7，6。
    matchNum = [2, 5, 5, 4, 5, 6, 3, 7, 6]
    # 用来存放每个数字的最大位数
    maxNum = [0] * m
    # 用来存放每个数字的最大位数的数字
    maxDigit = [0] * m
    # 用来存放每个数字的最大位数的数字的火柴棒数量
    maxDigitMatchNum = [0] * m
    # 用来存放每个数字的最大位数的数字的火柴棒数量的余数
    maxDigitMatchNumMod = [0] * m
    # 用来存放每个数字的最大位数的数字的火柴棒数量的商
    maxDigitMatchNumDiv = [0] * m
    # 用来存放每个数字的最大位数的数字的火柴棒数量的商的余数
    maxDigitMatchNumDivMod = [0] * m
    # 用来存放每个数字的最大位数的数字的火柴棒数量的商的商
    maxDigitMatchNumDivDiv = [0] * m
    # 用来存放每个数字的最大位数的数字的火柴棒数量的商的商的余数
    maxDigitMatchNumDivDivMod = [0] * m
    # 每个数字的最大位数
    for i in range(m):
        maxNum[i] = n / matchNum[a[i] - 1]
    # 每个数字的最大位数的数字
    for i in range(m):
        maxDigit[i] = maxNum[i] / 10
    # 每个数字的最大位数的数字的火柴棒数量
    for i in

if __name__ == '__main__':
    findMaxNum()