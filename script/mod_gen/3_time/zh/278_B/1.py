def main():
    #数据输入
    h,m = map(int,input().split())
    #数据处理
    if m < 10:
        m = "0" + str(m)
    else:
        m = str(m)
    if h < 10:
        h = "0" + str(h)
    else:
        h = str(h)
    #数据输出
    if h == "00":
        if m == "00":
            print("01:01")
        else:
            print("00:"+m)
    elif h == "01":
        if m == "01":
            print("01:10")
        else:
            print("01:"+m)
    elif h == "02":
        if m == "02":
            print("02:20")
        else:
            print("02:"+m)
    elif h == "03":
        if m == "03":
            print("03:30")
        else:
            print("03:"+m)
    elif h == "04":
        if m == "04":
            print("04:40")
        else:
            print("04:"+m)
    elif h == "05":
        if m == "05":
            print("05:50")
        else:
            print("05:"+m)
    elif h == "06":
        if m == "06":
            print("06:06")
        else:
            print("06:"+m)
    elif h == "07":
        if m == "07":
            print("07:07")
        else:
            print("07:"+m)
    elif h == "08":
        if m == "08":
            print("08:08")
        else:
            print("08:"+m)
    elif h == "09":
        if m == "09":
            print("09:09")
        else:
            print("09:"+m)
    elif h == "10":
        if m == "10":
            print("10:01")
        else:
            print("10:"+m)
    elif h == "11":
        if m == "11":
            print("11:11")
        else:
            print("11:"+m)
    elif h == "12":
        if m == "12":
            print("12:21")
        else:
            print("12:"+m)
    elif h == "13":
        if m == "13":
            print("13

if __name__ == '__main__':
    main()