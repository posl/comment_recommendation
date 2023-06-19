def main():
    # 输入
    S = input()
    #分割字符串
    S = S.split('/')
    # 年月日
    year = int(S[0])
    month = int(S[1])
    day = int(S[2])
    # 判断
    if year < 2019:
        print('Heisei')
    elif year == 2019:
        if month < 4:
            print('Heisei')
        elif month == 4:
            if day <= 30:
                print('Heisei')
            else:
                print('TBD')
        else:
            print('TBD')
    else:
        print('TBD')
