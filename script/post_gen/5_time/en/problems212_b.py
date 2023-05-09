Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    pin = input()
    if pin[0] == pin[1] and pin[1] == pin[2] and pin[2] == pin[3]:
        print("Weak")
    elif (int(pin[1]) - int(pin[0]) == 1 or int(pin[1]) - int(pin[0]) == -9) and (int(pin[2]) - int(pin[1]) == 1 or int(pin[2]) - int(pin[1]) == -9) and (int(pin[3]) - int(pin[2]) == 1 or int(pin[3]) - int(pin[2]) == -9):
        print("Weak")
    else:
        print("Strong")

=======
Suggestion 2

def main():
    pin = input()
    weak = True
    if pin[0] == pin[1] == pin[2] == pin[3]:
        weak = True
    else:
        for i in range(3):
            if pin[i+1] != str((int(pin[i]) + 1) % 10):
                weak = False
                break
    if weak:
        print("Weak")
    else:
        print("Strong")

=======
Suggestion 3

def main():
    pin = input()
    if (pin[0] == pin[1] == pin[2] == pin[3]) or (int(pin[1]) == (int(pin[0]) + 1) % 10 and int(pin[2]) == (int(pin[1]) + 1) % 10 and int(pin[3]) == (int(pin[2]) + 1) % 10):
        print('Weak')
    else:
        print('Strong')

=======
Suggestion 4

def weak_or_strong(pin):
    if pin[0] == pin[1] and pin[1] == pin[2] and pin[2] == pin[3]:
        return "Weak"
    else:
        if (int(pin[0]) + 1) % 10 == int(pin[1]) and (int(pin[1]) + 1) % 10 == int(pin[2]) and (int(pin[2]) + 1) % 10 == int(pin[3]):
            return "Weak"
        else:
            return "Strong"

=======
Suggestion 5

def problem():
    pin = input()
    if pin[0] == pin[1] == pin[2] == pin[3]:
        print("Weak")
        return
    for i in range(3):
        if (int(pin[i])+1)%10 != int(pin[i+1]):
            print("Strong")
            return
    print("Weak")
    return

problem()

=======
Suggestion 6

def main():
    input_str = input()
    input_list = list(input_str)
    if (input_list[0] == input_list[1] and input_list[1] == input_list[2] and input_list[2] == input_list[3]):
        print("Weak")
    else:
        weak = False
        for i in range(0, 3):
            if (int(input_list[i]) != 9):
                if (int(input_list[i]) + 1 != int(input_list[i + 1])):
                    weak = True
                    break
            else:
                if (int(input_list[i + 1]) != 0):
                    weak = True
                    break
        if (weak):
            print("Strong")
        else:
            print("Weak")

=======
Suggestion 7

def is_weak(pin):
    if len(set(pin)) == 1:
        return True
    for i in range(len(pin) - 1):
        if int(pin[i]) + 1 != int(pin[i + 1]) and not (pin[i] == '9' and pin[i + 1] == '0'):
            return False
    return True

=======
Suggestion 8

def main():
    # Take input
    s = input()
    # Check if all digits are the same
    if s[0] == s[1] == s[2] == s[3]:
        print('Weak')
        return
    # Check if digits are in ascending order
    if (int(s[0])+1)%10 == int(s[1]) and (int(s[1])+1)%10 == int(s[2]) and (int(s[2])+1)%10 == int(s[3]):
        print('Weak')
        return
    # Print result
    print('Strong')

=======
Suggestion 9

def isWeakPin(pin):
    if all(pin[0] == x for x in pin):
        return True
    for i in range(1, 4):
        if int(pin[i]) != (int(pin[i-1]) + 1) % 10:
            return False
    return True

pin = input()

=======
Suggestion 10

def get_input():
    return input()
