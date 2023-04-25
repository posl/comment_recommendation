Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    pin = input()
    if pin[0] == pin[1] == pin[2] == pin[3]:
        print("Weak")
    elif pin[0] == pin[1] and pin[2] == pin[3] and int(pin[1]) == (int(pin[2]) + 1) % 10:
        print("Weak")
    elif pin[0] == pin[2] and pin[1] == pin[3] and int(pin[2]) == (int(pin[1]) + 1) % 10:
        print("Weak")
    elif pin[0] == pin[3] and pin[1] == pin[2] and int(pin[3]) == (int(pin[1]) + 1) % 10:
        print("Weak")
    else:
        print("Strong")

=======
Suggestion 2

def main():
    pin = input()
    if pin[0] == pin[1] == pin[2] == pin[3]:
        print("Weak")
    elif pin[0] == pin[1] and pin[1] == pin[2] and pin[2] == pin[3]:
        print("Weak")
    elif pin[0] == pin[1] and pin[2] == pin[3] and pin[1] == str(int(pin[2]) - 1):
        print("Weak")
    elif pin[0] == str(int(pin[1]) - 1) and pin[1] == str(int(pin[2]) - 1) and pin[2] == str(int(pin[3]) - 1):
        print("Weak")
    elif pin[0] == str(int(pin[1]) - 1) and pin[1] == str(int(pin[2]) - 1) and pin[2] == str(int(pin[3]) - 1):
        print("Weak")
    elif pin[0] == str(int(pin[1]) - 1) and pin[1] == str(int(pin[2]) - 1) and pin[2] == str(int(pin[3]) - 1):
        print("Weak")
    elif pin[0] == str(int(pin[1]) - 1) and pin[1] == str(int(pin[2]) - 1) and pin[2] == str(int(pin[3]) - 1):
        print("Weak")
    elif pin[0] == str(int(pin[1]) - 1) and pin[1] == str(int(pin[2]) - 1) and pin[2] == str(int(pin[3]) - 1):
        print("Weak")
    elif pin[0] == str(int(pin[1]) - 1) and pin[1] == str(int(pin[2]) - 1) and pin[2] == str(int(pin[3]) - 1):
        print("Weak")
    elif pin[0] == str(int(pin[1]) - 1) and pin[1] == str(int(pin[2]) - 1) and pin[2] == str(int(pin[3]) - 1):
        print("Weak")
    elif pin[0] == str(int(pin[

=======
Suggestion 3

def main():
    pin = input()
    if pin[0] == pin[1] == pin[2] == pin[3]:
        print("Weak")
    elif pin[0] == pin[1] and pin[2] == pin[3] and pin[1] == str((int(pin[2]) - 1) % 10):
        print("Weak")
    elif pin[0] == pin[2] and pin[1] == pin[3] and pin[2] == str((int(pin[1]) - 1) % 10):
        print("Weak")
    elif pin[0] == pin[3] and pin[1] == pin[2] and pin[3] == str((int(pin[1]) - 1) % 10):
        print("Weak")
    else:
        print("Strong")

main()

=======
Suggestion 4

def isWeak(pin):
    if pin[0] == pin[1] == pin[2] == pin[3]:
        return True
    for i in range(3):
        if pin[i] == '9':
            if pin[i+1] != '0':
                return False
        elif int(pin[i]) + 1 != int(pin[i+1]):
            return False
    return True

pin = input()

=======
Suggestion 5

def is_weak_pin(pin):
    if pin[0] == pin[1] == pin[2] == pin[3]:
        return True
    for i in range(3):
        if pin[i+1] != str((int(pin[i])+1)%10):
            return False
    return True

pin = input()

=======
Suggestion 6

def main():
    #write your code below this line
    pin = input()
    if pin[0] == pin[1] == pin[2] == pin[3]:
        print('Weak')
    elif (int(pin[0]) + 1) % 10 == int(pin[1]) and (int(pin[1]) + 1) % 10 == int(pin[2]) and (int(pin[2]) + 1) % 10 == int(pin[3]):
        print('Weak')
    else:
        print('Strong')

=======
Suggestion 7

def is_weak(pin):
    return pin[0] == pin[1] == pin[2] == pin[3] or \
        (pin[0] == pin[1] == pin[2] and pin[3] == str((int(pin[2]) + 1) % 10)) or \
        (pin[1] == pin[2] == pin[3] and pin[0] == str((int(pin[3]) + 1) % 10))

pin = input()
print('Weak' if is_weak(pin) else 'Strong')

=======
Suggestion 8

def check_pin(pin):
    if pin[0] == pin[1] == pin[2] == pin[3]:
        return "Weak"
    elif (int(pin[0]) == (int(pin[1]) - 1) % 10) and (int(pin[1]) == (int(pin[2]) - 1) % 10) and (int(pin[2]) == (int(pin[3]) - 1) % 10):
        return "Weak"
    else:
        return "Strong"

pin = input()
print(check_pin(pin))

I am a 3rd year student of Computer Science and Engineering at the University of Moratuwa. I am currently doing my internship at the University of Moratuwa.

=======
Suggestion 9

def main():
    #input
    pin = input()

    #compute
    if pin[0] == pin[1] == pin[2] == pin[3]:
        ans = 'Weak'
    elif int(pin[0]) == int(pin[1])-1 and int(pin[1]) == int(pin[2])-1 and int(pin[2]) == int(pin[3])-1:
        ans = 'Weak'
    elif int(pin[0]) == 9 and int(pin[1]) == 0 and int(pin[2]) == 1 and int(pin[3]) == 2:
        ans = 'Weak'
    else:
        ans = 'Strong'
    #output
    print(ans)

main()

=======
Suggestion 10

def main():
    #input
    X = input()

    #compute
    if X[0]==X[1]==X[2]==X[3]:
        ans = 'Weak'
    elif int(X[1])-int(X[0]) == 1 and int(X[2])-int(X[1]) == 1 and int(X[3])-int(X[2]) == 1:
        ans = 'Weak'
    elif int(X[1])-int(X[0]) == -9 and int(X[2])-int(X[1]) == -9 and int(X[3])-int(X[2]) == -9:
        ans = 'Weak'
    else:
        ans = 'Strong'

    #output
    print(ans)
