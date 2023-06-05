Synthesizing 10/10 solutions

=======
Suggestion 1

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

=======
Suggestion 2

def main():
    x = input()
    if x[0] == x[1] and x[1] == x[2] and x[2] == x[3]:
        print("Weak")
    elif (int(x[1]) == (int(x[0]) + 1) % 10 and int(x[2]) == (int(x[1]) + 1) % 10 and int(x[3]) == (int(x[2]) + 1) % 10):
        print("Weak")
    else:
        print("Strong")

=======
Suggestion 3

def check_weakness(pin):
    if pin[0] == pin[1] and pin[1] == pin[2] and pin[2] == pin[3]:
        return True
    if (int(pin[0]) + 1) % 10 == int(pin[1]) and (int(pin[1]) + 1) % 10 == int(pin[2]) and (int(pin[2]) + 1) % 10 == int(pin[3]):
        return True
    return False

=======
Suggestion 4

def is_weak(pin):
    if pin[0] == pin[1] and pin[1] == pin[2] and pin[2] == pin[3]:
        return True
    if (int(pin[0]) + 1) % 10 == int(pin[1]) and (int(pin[1]) + 1) % 10 == int(pin[2]) and (int(pin[2]) + 1) % 10 == int(pin[3]):
        return True
    return False

=======
Suggestion 5

def main():
    pin = str(input())
    if pin[0] == pin[1] and pin[1] == pin[2] and pin[2] == pin[3]:
        print("Weak")
    elif (int(pin[0]) + 1) % 10 == int(pin[1]) and (int(pin[1]) + 1) % 10 == int(pin[2]) and (int(pin[2]) + 1) % 10 == int(pin[3]):
        print("Weak")
    else:
        print("Strong")

=======
Suggestion 6

def main():
    pin = input()
    if pin[0] == pin[1] == pin[2] == pin[3]:
        print('Weak')
    else:
        for i in range(3):
            if pin[i] == '9':
                if pin[i+1] != '0':
                    print('Strong')
                    return
            elif pin[i+1] != str(int(pin[i]) + 1):
                print('Strong')
                return
        print('Weak')

=======
Suggestion 7

def main():
    pin = input()
    if pin[0] == pin[1] == pin[2] == pin[3]:
        print("Weak")
    elif (int(pin[0]) + 1) % 10 == int(pin[1]) and (int(pin[1]) + 1) % 10 == int(pin[2]) and (int(pin[2]) + 1) % 10 == int(pin[3]):
        print("Weak")
    else:
        print("Strong")

=======
Suggestion 8

def main():
    pin = input()
    weak = True
    for i in range(3):
        if pin[i] != pin[i+1]:
            weak = False
            break
    if weak:
        print("Weak")
        return
    weak = True
    for i in range(3):
        if int(pin[i]) != (int(pin[i+1]) + 1) % 10:
            weak = False
            break
    if weak:
        print("Weak")
    else:
        print("Strong")

=======
Suggestion 9

def main():
    pin = input()
    if pin[0] == pin[1] and pin[1] == pin[2] and pin[2] == pin[3]:
        print("Weak")
    elif int(pin[1]) == (int(pin[0]) + 1) % 10 and int(pin[2]) == (int(pin[1]) + 1) % 10 and int(pin[3]) == (int(pin[2]) + 1) % 10:
        print("Weak")
    else:
        print("Strong")

=======
Suggestion 10

def main():
    pin = input()
    weak = True
    if pin[0] == pin[1] and pin[1] == pin[2] and pin[2] == pin[3]:
        weak = True
    elif pin[0] == '9' and pin[1] == '0' and pin[2] == '1':
        weak = True
    elif pin[0] == '0' and pin[1] == '9' and pin[2] == '8':
        weak = True
    elif pin[0] == pin[1] and pin[1] == pin[2]:
        weak = True
    elif pin[1] == pin[2] and pin[2] == pin[3]:
        weak = True
    else:
        weak = False
    if weak:
        print('Weak')
    else:
        print('Strong')
