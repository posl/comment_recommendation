Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    pin = input()
    if pin[0] == pin[1] == pin[2] == pin[3]:
        print('Weak')
    else:
        if (int(pin[0])+1)%10 == int(pin[1]) and (int(pin[1])+1)%10 == int(pin[2]) and (int(pin[2])+1)%10 == int(pin[3]):
            print('Weak')
        else:
            print('Strong')

=======
Suggestion 2

def main():
    pin = input()
    if pin[0] == pin[1] == pin[2] == pin[3]:
        print("Weak")
    elif (int(pin[1]) == (int(pin[0])+1)%10 and int(pin[2]) == (int(pin[1])+1)%10 and int(pin[3]) == (int(pin[2])+1)%10) or (int(pin[0]) == 9 and int(pin[1]) == 0 and int(pin[2]) == 1 and int(pin[3]) == 2):
        print("Weak")
    else:
        print("Strong")

=======
Suggestion 3

def main():
    pin = input()
    if pin[0] == pin[1] and pin[1] == pin[2] and pin[2] == pin[3]:
        print("Weak")
    else:
        flag = True
        for i in range(3):
            if pin[i] == '9':
                if pin[i+1] != '0':
                    flag = False
                    break
            else:
                if int(pin[i]) + 1 != int(pin[i+1]):
                    flag = False
                    break
        if flag:
            print("Weak")
        else:
            print("Strong")

=======
Suggestion 4

def main():
    pin = input()
    if pin[0] == pin[1] and pin[1] == pin[2] and pin[2] == pin[3]:
        print('Weak')
    elif (int(pin[1]) + 1) % 10 == int(pin[0]) and (int(pin[2]) + 1) % 10 == int(pin[1]) and (int(pin[3]) + 1) % 10 == int(pin[2]):
        print('Weak')
    else:
        print('Strong')

=======
Suggestion 5

def is_same(a,b,c,d):
    return a==b and b==c and c==d

=======
Suggestion 6

def main():
    pin = input()
    if pin[0] == pin[1] == pin[2] == pin[3]:
        print("Weak")
        return
    if (int(pin[0]) + 1) % 10 == int(pin[1]) and (int(pin[1]) + 1) % 10 == int(pin[2]) and (int(pin[2]) + 1) % 10 == int(pin[3]):
        print("Weak")
        return
    print("Strong")
    return

=======
Suggestion 7

def main():
    pin = input()
    weak = True
    if pin[0] == pin[1] and pin[1] == pin[2] and pin[2] == pin[3]:
        weak = True
    elif (int(pin[0]) + 1) % 10 == int(pin[1]) and (int(pin[1]) + 1) % 10 == int(pin[2]) and (int(pin[2]) + 1) % 10 == int(pin[3]):
        weak = True
    else:
        weak = False

    if weak:
        print("Weak")
    else:
        print("Strong")

=======
Suggestion 8

def main():
    pin = input()
    if len(set(pin)) == 1:
        print('Weak')
    elif pin in '0123 1234 2345 3456 4567 5678 6789 7890 8901 9012'.split():
        print('Weak')
    else:
        print('Strong')

=======
Suggestion 9

def main():
    pin = input()
    weak = "Weak"
    strong = "Strong"
    if pin[0] == pin[1] and pin[1] == pin[2] and pin[2] == pin[3]:
        print(weak)
        return
    if int(pin[0]) == (int(pin[1]) + 1) % 10 and int(pin[1]) == (int(pin[2]) + 1) % 10 and int(pin[2]) == (int(pin[3]) + 1) % 10:
        print(weak)
        return
    print(strong)

=======
Suggestion 10

def main():
    s = input()
    if s[0] == s[1] == s[2] == s[3]:
        print("Weak")
        return
    if (int(s[0]) + 1) % 10 == int(s[1]) and (int(s[1]) + 1) % 10 == int(s[2]) and (int(s[2]) + 1) % 10 == int(s[3]):
        print("Weak")
        return
    print("Strong")
