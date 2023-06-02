Synthesizing 10/10 solutions

=======
Suggestion 1

def is_weak(pin):
    if pin[0] == pin[1] and pin[1] == pin[2] and pin[2] == pin[3]:
        return True
    if pin[3] == (int(pin[2]) + 1) % 10 and pin[2] == (int(pin[1]) + 1) % 10 and pin[1] == (int(pin[0]) + 1) % 10:
        return True
    return False

=======
Suggestion 2

def main():
    pin = input()
    if pin[0] == pin[1] == pin[2] == pin[3]:
        print('Weak')
    elif (int(pin[1]) + 1) % 10 == int(pin[0]) and (int(pin[2]) + 1) % 10 == int(pin[1]) and (int(pin[3]) + 1) % 10 == int(pin[2]):
        print('Weak')
    else:
        print('Strong')

=======
Suggestion 3

def main():
    pin = input()
    if pin[0] == pin[1] and pin[1] == pin[2] and pin[2] == pin[3]:
        print('Weak')
    elif (int(pin[0]) + 1) % 10 == int(pin[1]) and (int(pin[1]) + 1) % 10 == int(pin[2]) and (int(pin[2]) + 1) % 10 == int(pin[3]):
        print('Weak')
    else:
        print('Strong')

=======
Suggestion 4

def main():
    pin = input()
    if pin[0] == pin[1] and pin[1] == pin[2] and pin[2] == pin[3]:
        print('Weak')
    else:
        for i in range(3):
            if (int(pin[i]) + 1) % 10 != int(pin[i+1]):
                break
        else:
            print('Weak')
            return
        print('Strong')

=======
Suggestion 5

def main():
    pin = input()
    if pin[0] == pin[1] == pin[2] == pin[3]:
        print('Weak')
    elif (int(pin[0]) + 1) % 10 == int(pin[1]) and (int(pin[1]) + 1) % 10 == int(pin[2]) and (int(pin[2]) + 1) % 10 == int(pin[3]):
        print('Weak')
    else:
        print('Strong')

=======
Suggestion 6

def main():
    pin = input()
    weak = True
    if pin[0] == pin[1] and pin[1] == pin[2] and pin[2] == pin[3]:
        weak = True
    else:
        for i in range(3):
            if int(pin[i]) == 9 and int(pin[i+1]) == 0:
                weak = True
            elif int(pin[i]) + 1 == int(pin[i+1]):
                weak = True
            else:
                weak = False
                break
    if weak:
        print("Weak")
    else:
        print("Strong")

=======
Suggestion 7

def main():
    pin = input()
    if pin[0] == pin[1] and pin[1] == pin[2] and pin[2] == pin[3]:
        print("Weak")
        return
    for i in range(3):
        if pin[i] == '9':
            if pin[i+1] != '0':
                print("Strong")
                return
        elif str(int(pin[i]) + 1) != pin[i+1]:
            print("Strong")
            return
    print("Weak")

=======
Suggestion 8

def main():
    # 读入数据
    input_line = input()
    # 解析数据
    x1 = int(input_line[0])
    x2 = int(input_line[1])
    x3 = int(input_line[2])
    x4 = int(input_line[3])

    # 逻辑处理
    if (x1 == x2 and x2 == x3 and x3 == x4):
        print("Weak")
    elif ((x2 == (x1 + 1) % 10) and (x3 == (x2 + 1) % 10) and (x4 == (x3 + 1) % 10)):
        print("Weak")
    else:
        print("Strong")

=======
Suggestion 9

def main():
    pin = input()
    if pin[0] == pin[1] == pin[2] == pin[3]:
        print("Weak")
        return
    if (int(pin[0])+1)%10 == int(pin[1]) and (int(pin[1])+1)%10 == int(pin[2]) and (int(pin[2])+1)%10 == int(pin[3]):
        print("Weak")
        return
    print("Strong")
    return

=======
Suggestion 10

def main():
    s = input()
    if s[0] == s[1] and s[1] == s[2] and s[2] == s[3]:
        print("Weak")
        return
    if (int(s[0])+1)%10 == int(s[1]) and (int(s[1])+1)%10 == int(s[2]) and (int(s[2])+1)%10 == int(s[3]):
        print("Weak")
        return
    print("Strong")
