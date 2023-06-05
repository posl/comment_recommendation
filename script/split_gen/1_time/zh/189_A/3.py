def main():
    print("请输入三个大写的英文字母，以空格隔开：")
    str = input()
    strList = str.split(" ")
    if strList[0] == strList[1] == strList[2]:
        print("Won")
    else:
        print("Lost")
