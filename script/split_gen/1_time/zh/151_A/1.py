def main():
    c = input("请输入一个小写英文字母：")
    if c == 'z':
        print("输入的字母是z，没有后面的字母")
    else:
        print("输入的字母是%s，它后面的字母是%s"%(c,chr(ord(c)+1)))
