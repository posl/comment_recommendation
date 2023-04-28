Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    pin = input()
    weak = True
    if pin[0] == pin[1] and pin[1] == pin[2] and pin[2] == pin[3]:
        weak = True
    else:
        weak = False
        for i in range(3):
            if (int(pin[i])+1)%10 != int(pin[i+1]):
                weak = True
                break
    if weak:
        print("Weak")
    else:
        print("Strong")

=======
Suggestion 2

def main():
    pin = input()
    if pin[0] == pin[1] == pin[2] == pin[3]:
        print('Weak')
    elif (int(pin[0]) + 1) % 10 == int(pin[1]) and (int(pin[1]) + 1) % 10 == int(pin[2]) and (int(pin[2]) + 1) % 10 == int(pin[3]):
        print('Weak')
    else:
        print('Strong')

=======
Suggestion 3

def main():
    s = input()
    if s[0] == s[1] == s[2] == s[3]:
        print("Weak")
    elif (int(s[0])+1)%10 == int(s[1]) and (int(s[1])+1)%10 == int(s[2]) and (int(s[2])+1)%10 == int(s[3]):
        print("Weak")
    else:
        print("Strong")

=======
Suggestion 4

def main():
    pin = input()
    if pin[0] == pin[1] == pin[2] == pin[3]:
        print("Weak")
    elif pin[1] == str((int(pin[0])+1)%10) and pin[2] == str((int(pin[1])+1)%10) and pin[3] == str((int(pin[2])+1)%10):
        print("Weak")
    else:
        print("Strong")

=======
Suggestion 5

def main():
    s = input()
    if s[0] == s[1] == s[2] == s[3]:
        print('Weak')
    elif int(s[1]) == (int(s[0])+1)%10 and int(s[2]) == (int(s[1])+1)%10 and int(s[3]) == (int(s[2])+1)%10:
        print('Weak')
    else:
        print('Strong')

=======
Suggestion 6

def main():
    pin = input()
    if pin[0] == pin[1] == pin[2] == pin[3]:
        print('Weak')
        return
    for i in range(3):
        if int(pin[i]) == 9 and int(pin[i+1]) == 0:
            continue
        if int(pin[i]) + 1 == int(pin[i+1]):
            continue
        print('Strong')
        return
    print('Weak')

=======
Suggestion 7

def main():
    pin = input()
    weak = True
    if pin[0] == pin[1] == pin[2] == pin[3]:
        weak = True
    else:
        weak = False
        if pin[0] == '9' and pin[1] == '0' and pin[2] == '1' and pin[3] == '2':
            weak = True
        else:
            if pin[1] == str((int(pin[0])+1)%10) and pin[2] == str((int(pin[1])+1)%10) and pin[3] == str((int(pin[2])+1)%10):
                weak = True
    if weak:
        print('Weak')
    else:
        print('Strong')

=======
Suggestion 8

def problem():
    pin = input()
    weak = True
    if pin[0] == pin[1] == pin[2] == pin[3]:
        weak = True
    else:
        for i in range(3):
            if pin[i] == '9':
                if pin[i+1] != '0':
                    weak = False
                    break
            else:
                if int(pin[i])+1 != int(pin[i+1]):
                    weak = False
                    break
    if weak:
        print('Weak')
    else:
        print('Strong')

problem()

=======
Suggestion 9

def main():
    pin = input()
    if pin[0] == pin[1] == pin[2] == pin[3]:
        print('Weak')
    else:
        if int(pin[0]) == int(pin[1]) + 1 or int(pin[0]) == 0 and int(pin[1]) == 9:
            if int(pin[1]) == int(pin[2]) + 1 or int(pin[1]) == 0 and int(pin[2]) == 9:
                if int(pin[2]) == int(pin[3]) + 1 or int(pin[2]) == 0 and int(pin[3]) == 9:
                    print('Weak')
                else:
                    print('Strong')
            else:
                print('Strong')
        else:
            print('Strong')

=======
Suggestion 10

def checkWeak(pin):
    if pin == '0000':
        return True
    if pin[0] == pin[1] == pin[2] == pin[3]:
        return True
    if int(pin[1]) == (int(pin[0])+1)%10 and int(pin[2]) == (int(pin[1])+1)%10 and int(pin[3]) == (int(pin[2])+1)%10:
        return True
    return False

pin = input()
