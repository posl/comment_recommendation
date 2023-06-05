def main():
    x = int(input("请输入x的值："))
    if 0 <= x <= 10**5:
        print(100-x%100)
    else:
        print("输入的值不符合规范！")
