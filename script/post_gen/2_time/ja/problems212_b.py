Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x = input()
    if x[0] == x[1] and x[1] == x[2] and x[2] == x[3]:
        print("Weak")
    elif int(x[0]) == (int(x[1]) + 1) % 10 and int(x[1]) == (int(x[2]) + 1) % 10 and int(x[2]) == (int(x[3]) + 1) % 10:
        print("Weak")
    else:
        print("Strong")

=======
Suggestion 2

def main():
    x = input()
    if x[0] == x[1] and x[1] == x[2] and x[2] == x[3]:
        print("Weak")
    else:
        if x[0] == '9' and x[1] == '0':
            if x[2] == '1' and x[3] == '2':
                print("Weak")
            else:
                print("Strong")
        else:
            if x[0] == '8' and x[1] == '9':
                if x[2] == '0' and x[3] == '1':
                    print("Weak")
                else:
                    print("Strong")
            else:
                if x[0] == '7' and x[1] == '8':
                    if x[2] == '9' and x[3] == '0':
                        print("Weak")
                    else:
                        print("Strong")
                else:
                    if x[0] == '6' and x[1] == '7':
                        if x[2] == '8' and x[3] == '9':
                            print("Weak")
                        else:
                            print("Strong")
                    else:
                        if x[0] == '5' and x[1] == '6':
                            if x[2] == '7' and x[3] == '8':
                                print("Weak")
                            else:
                                print("Strong")
                        else:
                            if x[0] == '4' and x[1] == '5':
                                if x[2] == '6' and x[3] == '7':
                                    print("Weak")
                                else:
                                    print("Strong")
                            else:
                                if x[0] == '3' and x[1] == '4':
                                    if x[2] == '5' and x[3] == '6':
                                        print("Weak")
                                    else:
                                        print("Strong")
                                else:
                                    if x[0] == '2' and x[1] == '3':
                                        if x[2] == '4' and x[3] == '5':
                                            print("Weak")
                                        else:
                                            print("Strong")
                                    else:
                                        if x[0] == '1' and x[1] == '2':
                                            if x

=======
Suggestion 3

def main():
    X = input()
    if X[0]==X[1]==X[2]==X[3]:
        print('Weak')
    elif (int(X[0])+1)%10==int(X[1]) and (int(X[1])+1)%10==int(X[2]) and (int(X[2])+1)%10==int(X[3]):
        print('Weak')
    else:
        print('Strong')

=======
Suggestion 4

def main():
    X = input()
    if X[0] == X[1] == X[2] == X[3]:
        print("Weak")
        return
    if (int(X[0])+1)%10 == int(X[1]) and (int(X[1])+1)%10 == int(X[2]) and (int(X[2])+1)%10 == int(X[3]):
        print("Weak")
        return
    print("Strong")

=======
Suggestion 5

def main():
    s = input()
    if s[0] == s[1] == s[2] == s[3]:
        print("Weak")
        return
    for i in range(3):
        if int(s[i+1]) != (int(s[i])+1)%10:
            print("Strong")
            return
    print("Weak")
    return

=======
Suggestion 6

def main():
    X = input()
    if X[0] == X[1] == X[2] == X[3]:
        print('Weak')
    else:
        if (int(X[0])+1)%10 == int(X[1]) and (int(X[1])+1)%10 == int(X[2]) and (int(X[2])+1)%10 == int(X[3]):
            print('Weak')
        else:
            print('Strong')

=======
Suggestion 7

def main():
    s = input()
    if s[0] == s[1] == s[2] == s[3]:
        print('Weak')
    else:
        for i in range(3):
            if s[i] == '9':
                if s[i+1] != '0':
                    print('Strong')
                    exit()
            else:
                if int(s[i])+1 != int(s[i+1]):
                    print('Strong')
                    exit()
        print('Weak')

=======
Suggestion 8

def main():
    # input
    X = input()
    # compute
    is_weak = True
    if X[0] == X[1] and X[1] == X[2] and X[2] == X[3]:
        is_weak = True
    else:
        is_weak = False
    if (int(X[1])+1)%10 == int(X[2]) and (int(X[2])+1)%10 == int(X[3]):
        is_weak = True
    else:
        is_weak = False
    # output
    if is_weak:
        print("Weak")
    else:
        print("Strong")

=======
Suggestion 9

def main():
    # input
    X = input()

    # compute
    if (X[0]==X[1] and X[1]==X[2] and X[2]==X[3]) or (X[0]==X[1] and X[1]==X[2] and X[2]==X[3]) or (X[0]==X[1] and X[1]==X[2] and X[2]==X[3]) or (X[0]==X[1] and X[1]==X[2] and X[2]==X[3]) or (X[0]==X[1] and X[1]==X[2] and X[2]==X[3]) or (X[0]==X[1] and X[1]==X[2] and X[2]==X[3]) or (X[0]==X[1] and X[1]==X[2] and X[2]==X[3]) or (X[0]==X[1] and X[1]==X[2] and X[2]==X[3]):
        print("Weak")
    elif (int(X[0])+1)%10==int(X[1]) and (int(X[1])+1)%10==int(X[2]) and (int(X[2])+1)%10==int(X[3]):
        print("Weak")
    else:
        print("Strong")

=======
Suggestion 10

def checkWeakOrStrong(password):
    if password[0] == password[1] and password[1] == password[2] and password[2] == password[3]:
        print("Weak")
        return
    if int(password[0]) == 9 and int(password[1]) == 0 and int(password[2]) == 1 and int(password[3]) == 2:
        print("Weak")
        return
    if int(password[0]) == 8 and int(password[1]) == 9 and int(password[2]) == 0 and int(password[3]) == 1:
        print("Weak")
        return
    if int(password[0]) == 7 and int(password[1]) == 8 and int(password[2]) == 9 and int(password[3]) == 0:
        print("Weak")
        return
    if int(password[0]) == 6 and int(password[1]) == 7 and int(password[2]) == 8 and int(password[3]) == 9:
        print("Weak")
        return
    if int(password[0]) == 5 and int(password[1]) == 6 and int(password[2]) == 7 and int(password[3]) == 8:
        print("Weak")
        return
    if int(password[0]) == 4 and int(password[1]) == 5 and int(password[2]) == 6 and int(password[3]) == 7:
        print("Weak")
        return
    if int(password[0]) == 3 and int(password[1]) == 4 and int(password[2]) == 5 and int(password[3]) == 6:
        print("Weak")
        return
    if int(password[0]) == 2 and int(password[1]) == 3 and int(password[2]) == 4 and int(password[3]) == 5:
        print("Weak")
        return
    if int(password[0]) == 1 and int(password[1]) == 2 and int(password[2]) == 3 and int(password[3]) == 4:
        print("Weak")
        return
    if int(password[0]) == 0 and int(password[1]) == 1 and int(password[2]) == 2 and int(password[3]) == 3:
        print("
