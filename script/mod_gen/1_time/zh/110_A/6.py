def main(a, b, c):
    # 1. 3个数都为9的情况
    if a == 9 and b == 9 and c == 9:
        return 108
    # 2. 3个数都为1的情况
    if a == 1 and b == 1 and c == 1:
        return 12
    # 3. 2个数为9，1个数为1的情况
    if (a == 9 and b == 9 and c == 1) or (a == 9 and b == 1 and c == 9) or (a == 1 and b == 9 and c == 9):
        return 91
    # 4. 2个数为1，1个数为9的情况
    if (a == 1 and b == 1 and c == 9) or (a == 1 and b == 9 and c == 1) or (a == 9 and b == 1 and c == 1):
        return 19
    # 5. 2个数为9，1个数为2的情况
    if (a == 9 and b == 9 and c == 2) or (a == 9 and b == 2 and c == 9) or (a == 2 and b == 9 and c == 9):
        return 92
    # 6. 2个数为2，1个数为9的情况
    if (a == 2 and b == 2 and c == 9) or (a == 2 and b == 9 and c == 2) or (a == 9 and b == 2 and c == 2):
        return 29
    # 7. 2个数为9，1个数为3的情况
    if (a == 9 and b == 9 and c == 3) or (a == 9 and b == 3 and c == 9) or (a == 3 and b == 9 and c == 9):
        return 93
    # 8. 2个数为3，1个数为9的情

if __name__ == '__main__':
    main()