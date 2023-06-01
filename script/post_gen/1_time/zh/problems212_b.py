Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    pin = input()
    if pin[0] == pin[1] == pin[2] == pin[3]:
        print("Weak")
        return
    if (int(pin[1])+1)%10 == int(pin[0]) and (int(pin[2])+1)%10 == int(pin[1]) and (int(pin[3])+1)%10 == int(pin[2]):
        print("Weak")
        return
    print("Strong")
    return

=======
Suggestion 2

def main():
    pin = input()
    if pin[0] == pin[1] == pin[2] == pin[3]:
        print("Weak")
    elif (int(pin[0])+1)%10 == int(pin[1]) and (int(pin[1])+1)%10 == int(pin[2]) and (int(pin[2])+1)%10 == int(pin[3]):
        print("Weak")
    else:
        print("Strong")

=======
Suggestion 3

def main():
    pin = input()
    if pin[0] == pin[1] and pin[1] == pin[2] and pin[2] == pin[3]:
        print("Weak")
    elif (int(pin[0]) + 1) % 10 == int(pin[1]) and (int(pin[1]) + 1) % 10 == int(pin[2]) and (int(pin[2]) + 1) % 10 == int(pin[3]):
        print("Weak")
    else:
        print("Strong")

=======
Suggestion 4

def main():
    pin = input()
    if pin[0] == pin[1] and pin[1] == pin[2] and pin[2] == pin[3]:
        print("Weak")
    else:
        if (int(pin[0]) + 1) % 10 == int(pin[1]) and (int(pin[1]) + 1) % 10 == int(pin[2]) and (int(pin[2]) + 1) % 10 == int(pin[3]):
            print("Weak")
        else:
            print("Strong")

=======
Suggestion 5

def main():
    pin = input()
    if pin[0] == pin[1] and pin[1] == pin[2] and pin[2] == pin[3]:
        print('Weak')
    elif (int(pin[0]) + 1) % 10 == int(pin[1]) and (int(pin[1]) + 1) % 10 == int(pin[2]) and (int(pin[2]) + 1) % 10 == int(pin[3]):
        print('Weak')
    else:
        print('Strong')

=======
Suggestion 6

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

=======
Suggestion 7

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

=======
Suggestion 8

def main():
    pin = input()
    if pin == '0000' or pin == '1111' or pin == '2222' or pin == '3333' or pin == '4444' or pin == '5555' or pin == '6666' or pin == '7777' or pin == '8888' or pin == '9999':
        print('Weak')
    elif pin[0] == pin[1] and pin[1] == pin[2] and pin[2] == pin[3]:
        print('Weak')
    elif (int(pin[0]) + 1) % 10 == int(pin[1]) and (int(pin[1]) + 1) % 10 == int(pin[2]) and (int(pin[2]) + 1) % 10 == int(pin[3]):
        print('Weak')
    else:
        print('Strong')

=======
Suggestion 9

def main():
    s = input()
    if s[0] == s[1] == s[2] == s[3]:
        print('Weak')
        return
    for i in range(3):
        if (int(s[i]) + 1) % 10 != int(s[i+1]):
            print('Strong')
            return
    print('Weak')

=======
Suggestion 10

def main():
    pin = input()
    if pin[0] == pin[1] == pin[2] == pin[3]:
        print('Weak')
    elif pin[0] == str((int(pin[1]) + 1) % 10) and pin[1] == str((int(pin[2]) + 1) % 10) and pin[2] == str((int(pin[3]) + 1) % 10):
        print('Weak')
    else:
        print('Strong')
