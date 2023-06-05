def S(n):
    # 计算n的十进制数字之和
    n = str(n)
    sum = 0
    for i in n:
        sum += int(i)
    return sum

if __name__ == '__main__':
    S()