def main():
    # 输入
    pin = input()
    # 计算
    # 1. 四个数字都是一样的
    if pin[0] == pin[1] and pin[1] == pin[2] and pin[2] == pin[3]:
        print("Weak")
        return
    # 2. 对于每个整数i，如1≦i≦3，X_{i+1}跟随X_i。这里，对于每一个0≦ j≦ 8的j+1跟随j，而0跟随9。
    # 2.1 第一位数字跟随第四位数字
    if pin[0] == str((int(pin[3]) + 1) % 10):
        print("Weak")
        return
    # 2.2 第二位数字跟随第一位数字
    if pin[1] == str((int(pin[0]) + 1) % 10):
        print("Weak")
        return
    # 2.3 第三位数字跟随第二位数字
    if pin[2] == str((int(pin[1]) + 1) % 10):
        print("Weak")
        return
    # 2.4 第四位数字跟随第三位数字
    if pin[3] == str((int(pin[2]) + 1) % 10):
        print("Weak")
        return
    # 输出
    print("Strong")

if __name__ == '__main__':
    main()