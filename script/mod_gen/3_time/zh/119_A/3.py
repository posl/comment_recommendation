def main():
    # 读取输入
    S = input()
    # 请在下面编写你的代码
    year, month, day = S.split('/')
    year = int(year)
    month = int(month)
    day = int(day)
    if year < 2019:
        print('平成')
    elif year == 2019:
        if month < 4:
            print('平成')
        elif month == 4:
            if day <= 30:
                print('平成')
            else:
                print('TBD')
        else:
            print('TBD')
    else:
        print('TBD')

if __name__ == '__main__':
    main()