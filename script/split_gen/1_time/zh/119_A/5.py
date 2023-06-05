def main():
    # 日期输入
    date = input()
    # 年月日分离
    year, month, day = date.split('/')
    # 判断
    if int(year) < 2019:
        print('Heisei')
    elif int(year) == 2019 and int(month) < 4:
        print('Heisei')
    elif int(year) == 2019 and int(month) == 4 and int(day) <= 30:
        print('Heisei')
    else:
        print('TBD')
