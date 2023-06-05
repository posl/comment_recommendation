def main():
    # 读入数据
    str = input()
    # 处理数据
    # 切分字符串
    year, month, day = str.split("/")
    # 判断是否小于等于2019/04/30
    if year < "2019" or (year == "2019" and month < "04") or (year == "2019" and month == "04" and day <= "30"):
        print("平成")
    else:
        print("TBD")
