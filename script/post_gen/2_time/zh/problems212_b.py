Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # input
    pin = input()
    # check
    if pin[0] == pin[1] == pin[2] == pin[3]:
        print('Weak')
        return
    else:
        for i in range(3):
            if pin[i] == '9':
                if pin[i+1] != '0':
                    print('Strong')
                    return
            else:
                if pin[i+1] != str(int(pin[i])+1):
                    print('Strong')
                    return
    print('Weak')
    return

=======
Suggestion 2

def main():
    pin = input()
    if pin[0] == pin[1] and pin[1] == pin[2] and pin[2] == pin[3]:
        print('Weak')
    else:
        if (int(pin[0]) + 1) % 10 == int(pin[1]) and (int(pin[1]) + 1) % 10 == int(pin[2]) and (int(pin[2]) + 1) % 10 == int(pin[3]):
            print('Weak')
        else:
            print('Strong')

=======
Suggestion 3

def main():
    s = input()
    if s[0] == s[1] and s[1] == s[2] and s[2] == s[3]:
        print('Weak')
    else:
        for i in range(3):
            if (int(s[i])+1)%10 != int(s[i+1]):
                print('Strong')
                break
        else:
            print('Weak')

=======
Suggestion 4

def isWeak(pin):
    if pin[0] == pin[1] and pin[1] == pin[2] and pin[2] == pin[3]:
        return True
    elif (int(pin[1]) - int(pin[0]) + 10) % 10 == 1 and (int(pin[2]) - int(pin[1]) + 10) % 10 == 1 and (int(pin[3]) - int(pin[2]) + 10) % 10 == 1:
        return True
    else:
        return False

=======
Suggestion 5

def main():
    pin = input()
    if pin[0] == pin[1] and pin[1] == pin[2] and pin[2] == pin[3]:
        print("Weak")
    elif (int(pin[1]) + 1) % 10 == int(pin[0]) and (int(pin[2]) + 1) % 10 == int(pin[1]) and (int(pin[3]) + 1) % 10 == int(pin[2]):
        print("Weak")
    else:
        print("Strong")

=======
Suggestion 6

def main():
    pin = input()
    if pin[0] == pin[1] and pin[1] == pin[2] and pin[2] == pin[3]:
        print("Weak")
    elif (int(pin[0])+1)%10 == int(pin[1]) and (int(pin[1])+1)%10 == int(pin[2]) and (int(pin[2])+1)%10 == int(pin[3]):
        print("Weak")
    else:
        print("Strong")

=======
Suggestion 7

def main():
    pin = input()
    if pin[0] == pin[1] and pin[1] == pin[2] and pin[2] == pin[3]:
        print("Weak")
    else:
        if (int(pin[0])+1)%10 == int(pin[1]) and (int(pin[1])+1)%10 == int(pin[2]) and (int(pin[2])+1)%10 == int(pin[3]):
            print("Weak")
        else:
            print("Strong")

=======
Suggestion 8

def main():
    pin = input()
    if pin.count(pin[0]) == 4 or pin[0] == '9' and pin[1] == '0' and pin[2] == '1' and pin[3] == '2' or pin[0] == '0' and pin[1] == '1' and pin[2] == '2' and pin[3] == '3' or pin[0] == '1' and pin[1] == '2' and pin[2] == '3' and pin[3] == '4' or pin[0] == '2' and pin[1] == '3' and pin[2] == '4' and pin[3] == '5' or pin[0] == '3' and pin[1] == '4' and pin[2] == '5' and pin[3] == '6' or pin[0] == '4' and pin[1] == '5' and pin[2] == '6' and pin[3] == '7' or pin[0] == '5' and pin[1] == '6' and pin[2] == '7' and pin[3] == '8' or pin[0] == '6' and pin[1] == '7' and pin[2] == '8' and pin[3] == '9' or pin[0] == '7' and pin[1] == '8' and pin[2] == '9' and pin[3] == '0':
        print("Weak")
    else:
        print("Strong")

=======
Suggestion 9

def is_weak(PIN):
    if PIN == PIN[0]*4:
        return True
    else:
        for i in range(3):
            if PIN[i] == '9' and PIN[i+1] == '0':
                return True
            elif PIN[i+1] != str(int(PIN[i])+1):
                return False
        return True

PIN = input()
