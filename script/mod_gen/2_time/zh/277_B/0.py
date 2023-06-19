def main():
    num = int(input("请输入字符串个数:"))
    list = []
    for i in range(num):
        list.append(input("请输入字符串:"))
    if num == len(set(list)):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()