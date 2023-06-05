def main():
    # 读入数据
    pin = input()
    # 处理数据
    # 判断是否满足第一个条件
    if pin[0] == pin[1] and pin[1] == pin[2] and pin[2] == pin[3]:
        print("Weak")
        return
    # 判断是否满足第二个条件
    for i in range(3):
        if pin[i] == '9':
            if pin[i + 1] != '0':
                print("Strong")
                return
        elif pin[i + 1] != chr(ord(pin[i]) + 1):
            print("Strong")
            return
    # 输出结果
    print("Weak")

if __name__ == '__main__':
    main()