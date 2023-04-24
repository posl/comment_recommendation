Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    pin = input()
    if pin[0] == pin[1] == pin[2] == pin[3]:
        print('Weak')
    elif pin[0] == '9' and pin[1] == '0' and pin[2] == '1' and pin[3] == '2':
        print('Weak')
    elif pin[0] == '0' and pin[1] == '1' and pin[2] == '2' and pin[3] == '3':
        print('Weak')
    elif pin[0] == '1' and pin[1] == '2' and pin[2] == '3' and pin[3] == '4':
        print('Weak')
    elif pin[0] == '2' and pin[1] == '3' and pin[2] == '4' and pin[3] == '5':
        print('Weak')
    elif pin[0] == '3' and pin[1] == '4' and pin[2] == '5' and pin[3] == '6':
        print('Weak')
    elif pin[0] == '4' and pin[1] == '5' and pin[2] == '6' and pin[3] == '7':
        print('Weak')
    elif pin[0] == '5' and pin[1] == '6' and pin[2] == '7' and pin[3] == '8':
        print('Weak')
    elif pin[0] == '6' and pin[1] == '7' and pin[2] == '8' and pin[3] == '9':
        print('Weak')
    else:
        print('Strong')

main()

=======
Suggestion 2

def main():
    pin = input()
    if pin[0] == pin[1] == pin[2] == pin[3]:
        print("Weak")
    elif pin[0] == pin[1] and pin[1] == pin[2]:
        print("Weak")
    elif pin[1] == pin[2] and pin[2] == pin[3]:
        print("Weak")
    elif pin[0] == pin[1] and pin[2] == pin[3]:
        print("Weak")
    elif pin[0] == str(int(pin[1])-1) and pin[1] == str(int(pin[2])-1) and pin[2] == str(int(pin[3])-1):
        print("Weak")
    elif pin[0] == "9" and pin[1] == "0" and pin[2] == "1" and pin[3] == "2":
        print("Weak")
    else:
        print("Strong")

main()

=======
Suggestion 3

def main():
    pin = input()
    if pin[0] == pin[1] == pin[2] == pin[3]:
        print('Weak')
        return
    for i in range(3):
        if int(pin[i+1]) - int(pin[i]) == 1 or int(pin[i+1]) - int(pin[i]) == -9:
            continue
        else:
            print('Strong')
            return
    print('Weak')

=======
Suggestion 4

def main():
    x = input()
    if x[0] == x[1] == x[2] == x[3]:
        print("Weak")
    elif x[0] == "9" and x[1] == "0" and x[2] == "1" and x[3] == "2":
        print("Weak")
    elif x[0] == str(int(x[1])-1) and x[1] == str(int(x[2])-1) and x[2] == str(int(x[3])-1):
        print("Weak")
    else:
        print("Strong")

=======
Suggestion 5

def main():
    pin = input()
    if pin[0] == pin[1] == pin[2] == pin[3]:
        print('Weak')
        return
    if pin[0] == '9' and pin[1] == '0':
        if pin[2] == '1' and pin[3] == '2':
            print('Weak')
            return
    if pin[0] == '0' and pin[1] == '1':
        if pin[2] == '2' and pin[3] == '3':
            print('Weak')
            return
    if pin[0] == '1' and pin[1] == '2':
        if pin[2] == '3' and pin[3] == '4':
            print('Weak')
            return
    if pin[0] == '2' and pin[1] == '3':
        if pin[2] == '4' and pin[3] == '5':
            print('Weak')
            return
    if pin[0] == '3' and pin[1] == '4':
        if pin[2] == '5' and pin[3] == '6':
            print('Weak')
            return
    if pin[0] == '4' and pin[1] == '5':
        if pin[2] == '6' and pin[3] == '7':
            print('Weak')
            return
    if pin[0] == '5' and pin[1] == '6':
        if pin[2] == '7' and pin[3] == '8':
            print('Weak')
            return
    if pin[0] == '6' and pin[1] == '7':
        if pin[2] == '8' and pin[3] == '9':
            print('Weak')
            return
    if pin[0] == '7' and pin[1] == '8':
        if pin[2] == '9' and pin[3] == '0':
            print('Weak')
            return
    if pin[0] == '8' and pin[1] == '9':
        if pin[2] == '0' and pin[3] == '1':
            print('Weak')
            return
    print('Strong

=======
Suggestion 6

def main():
    line = input()
    if line[0] == line[1] == line[2] == line[3]:
        print("Weak")
    elif int(line[1]) == (int(line[0]) + 1) % 10 and int(line[2]) == (int(line[1]) + 1) % 10 and int(line[3]) == (int(line[2]) + 1) % 10:
        print("Weak")
    else:
        print("Strong")

=======
Suggestion 7

def isWeak(pin):
    for i in range(1,4):
        if pin[i] != pin[i-1]:
            break
    else:
        return True
    for i in range(1,4):
        if pin[i] != str((int(pin[i-1])+1)%10):
            return False
    return True

pin = input()

=======
Suggestion 8

def main():
    # Read a string:
    s = input()
    # Print a string:
    #print(s)
    if s[0] == s[1] and s[1] == s[2] and s[2] == s[3]:
        print("Weak")
    elif s[0] == '9' and s[1] == '0' and s[2] == '1' and s[3] == '2':
        print("Weak")
    elif int(s[0]) + 1 == int(s[1]) and int(s[1]) + 1 == int(s[2]) and int(s[2]) + 1 == int(s[3]):
        print("Weak")
    else:
        print("Strong")

=======
Suggestion 9

def main():
    #input
    pin = input()
    #compute
    if pin[0] == pin[1] == pin[2] == pin[3]:
        ans = 'Weak'
    elif int(pin[0]) + 1 == int(pin[1]) or int(pin[0]) == 9 and int(pin[1]) == 0:
        if int(pin[1]) + 1 == int(pin[2]) or int(pin[1]) == 9 and int(pin[2]) == 0:
            if int(pin[2]) + 1 == int(pin[3]) or int(pin[2]) == 9 and int(pin[3]) == 0:
                ans = 'Weak'
            else:
                ans = 'Strong'
        else:
            ans = 'Strong'
    else:
        ans = 'Strong'
    #output
    print(ans)

=======
Suggestion 10

def main():
    # Get input
    a, b, c, d = input()
    # Check if all digits are the same
    if (a == b and b == c and c == d):
        print("Weak")
    # Check if each digit follows the previous one
    elif (int(a) + 1 == int(b) or (a == "9" and b == "0")) and (int(b) + 1 == int(c) or (b == "9" and c == "0")) and (int(c) + 1 == int(d) or (c == "9" and d == "0")):
        print("Weak")
    else:
        print("Strong")
