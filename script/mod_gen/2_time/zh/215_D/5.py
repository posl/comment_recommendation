def findKthPermutation(s, k):
    if k == 1:
        return s
    length = len(s)
    if length == 1:
        return s
    #计算阶乘
    factorial = 1
    for i in range(1, length):
        factorial *= i
    #计算当前位
    quotient = k / factorial
    remainder = k % factorial
    if remainder == 0:
        quotient -= 1
        remainder = factorial
    #取当前位
    current_char = s[quotient]
    #取剩余字符串
    rest = s[:quotient] + s[quotient + 1:]
    #递归
    return current_char + findKthPermutation(rest, remainder)

if __name__ == '__main__':
    findKthPermutation()