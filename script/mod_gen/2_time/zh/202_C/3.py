def main():
    # 获取输入内容
    str = input()
    # 旋转180度后的数字
    str180 = ""
    # 旋转180度后的数字
    str180 = str[::-1]
    # 旋转180度后的数字
    str180 = str180.replace("0", "a")
    str180 = str180.replace("1", "b")
    str180 = str180.replace("6", "c")
    str180 = str180.replace("8", "d")
    str180 = str180.replace("9", "e")
    str180 = str180.replace("a", "1")
    str180 = str180.replace("b", "0")
    str180 = str180.replace("c", "9")
    str180 = str180.replace("d", "8")
    str180 = str180.replace("e", "6")
    # 输出旋转180度后的数字
    print(str180)

if __name__ == '__main__':
    main()