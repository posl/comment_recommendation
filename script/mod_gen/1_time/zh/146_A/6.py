def main():
    # 读取输入
    s = input()
    # 请在此添加代码
    day = 0
    # 请在此添加代码
    if s == 'SUN':
        day = 7
    elif s == 'MON':
        day = 6
    elif s == 'TUE':
        day = 5
    elif s == 'WED':
        day = 4
    elif s == 'THU':
        day = 3
    elif s == 'FRI':
        day = 2
    elif s == 'SAT':
        day = 1
    # 请在此添加代码
    print(day)

if __name__ == '__main__':
    main()