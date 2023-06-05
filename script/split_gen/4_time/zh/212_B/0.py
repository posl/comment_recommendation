def main():
    # 输入
    pin = input()
    # 处理
    weak = True
    if pin[0] == pin[1] and pin[1] == pin[2] and pin[2] == pin[3]:
        weak = True
    elif int(pin[0]) + 1 == int(pin[1]) or (int(pin[0]) == 9 and int(pin[1]) == 0):
        if int(pin[1]) + 1 == int(pin[2]) or (int(pin[1]) == 9 and int(pin[2]) == 0):
            if int(pin[2]) + 1 == int(pin[3]) or (int(pin[2]) == 9 and int(pin[3]) == 0):
                weak = True
            else:
                weak = False
        else:
            weak = False
    else:
        weak = False
    # 输出
    if weak:
        print("Weak")
    else:
        print("Strong")
