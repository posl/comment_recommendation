Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    pin = input()
    if pin[0] == pin[1] == pin[2] == pin[3]:
        print("Weak")
    elif (int(pin[0]) + 1) % 10 == int(pin[1]) and (int(pin[1]) + 1) % 10 == int(pin[2]) and (int(pin[2]) + 1) % 10 == int(pin[3]):
        print("Weak")
    else:
        print("Strong")

=======
Suggestion 2

def main():
    pin = input()
    if pin[0] == pin[1] == pin[2] == pin[3]:
        print('Weak')
    elif int(pin[0]) + 1 == int(pin[1]) and int(pin[1]) + 1 == int(pin[2]) and int(pin[2]) + 1 == int(pin[3]):
        print('Weak')
    elif int(pin[0]) + 1 == int(pin[1]) and int(pin[1]) + 1 == int(pin[2]) and int(pin[3]) == 0:
        print('Weak')
    elif int(pin[0]) == 9 and int(pin[1]) == 0 and int(pin[2]) + 1 == int(pin[3]):
        print('Weak')
    else:
        print('Strong')

=======
Suggestion 3

def weak(pin):
    if pin[0] == pin[1] == pin[2] == pin[3]:
        return True
    for i in range(3):
        if (int(pin[i]) + 1) % 10 != int(pin[i + 1]):
            return False
    return True

pin = input()

=======
Suggestion 4

def main():
    pin = input()
    if pin[0] == pin[1] == pin[2] == pin[3]:
        print('Weak')
    elif (int(pin[0])+1) % 10 == int(pin[1]) and (int(pin[1])+1) % 10 == int(pin[2]) and (int(pin[2])+1) % 10 == int(pin[3]):
        print('Weak')
    else:
        print('Strong')

=======
Suggestion 5

def weak(pin):
    if pin[0] == pin[1] == pin[2] == pin[3]:
        return True
    for i in range(3):
        if pin[i] == '9' and pin[i+1] == '0':
            return True
        if int(pin[i]) + 1 != int(pin[i+1]):
            return False
    return True

pin = input()

=======
Suggestion 6

def is_weak(pin):
    return pin[0] == pin[1] == pin[2] == pin[3] or \
           pin[0] == pin[1] == pin[2] or \
           pin[1] == pin[2] == pin[3] or \
           pin[0] == pin[1] or \
           pin[1] == pin[2] or \
           pin[2] == pin[3]

pin = input()

=======
Suggestion 7

def checkWeak(pin):
    if pin[0] == pin[1] and pin[1] == pin[2] and pin[2] == pin[3]:
        return "Weak"
    for i in range(3):
        if int(pin[i+1]) == (int(pin[i]) + 1) % 10:
            continue
        else:
            return "Strong"
    return "Weak"

pin = input()
print(checkWeak(pin))

=======
Suggestion 8

def check_weak(pin):
    if pin[0] == pin[1] == pin[2] == pin[3]:
        return True
    for i in range(3):
        if pin[i+1] == '0':
            if pin[i] != '9':
                return False
        else:
            if pin[i] != str(int(pin[i+1])-1):
                return False
    return True

pin = input()

=======
Suggestion 9

def main():
    #input
    pin = input()
    #output
    if pin[0] == pin[1] == pin[2] == pin[3]:
        print('Weak')
    elif int(pin[0]) == (int(pin[1])-1)%10 == (int(pin[2])-1)%10 == (int(pin[3])-1)%10:
        print('Weak')
    else:
        print('Strong')

main()

=======
Suggestion 10

def checkWeakness(pin):
    if pin[0] == pin[1] == pin[2] == pin[3]:
        return True
    else:
        for i in range(0, 3):
            if pin[i+1] == str(int(pin[i]) + 1):
                continue
            else:
                return False
        return True

pin = input()
