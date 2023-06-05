def main():
    # 输入
    s = input()
    # 处理
    # 切分字符串
    s_list = s.split('/')
    # 判断
    if int(s_list[0]) < 2019:
        print('Heisei')
    elif int(s_list[0]) == 2019:
        if int(s_list[1]) < 4:
            print('Heisei')
        elif int(s_list[1]) == 4:
            if int(s_list[2]) <= 30:
                print('Heisei')
            else:
                print('TBD')
        else:
            print('TBD')
    else:
        print('TBD')
    # 输出

if __name__ == '__main__':
    main()