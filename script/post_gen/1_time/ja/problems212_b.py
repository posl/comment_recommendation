Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x = input()
    if x[0] == x[1] and x[1] == x[2] and x[2] == x[3]:
        print("Weak")
        return
    if (int(x[0]) + 1) % 10 == int(x[1]) and (int(x[1]) + 1) % 10 == int(x[2]) and (int(x[2]) + 1) % 10 == int(x[3]):
        print("Weak")
        return
    print("Strong")

=======
Suggestion 2

def main():
    X = input()
    if X[0] == X[1] and X[1] == X[2] and X[2] == X[3]:
        print("Weak")
        return
    for i in range(3):
        if (int(X[i]) + 1) % 10 != int(X[i+1]):
            print("Strong")
            return
    print("Weak")

=======
Suggestion 3

def main():
    s = input()
    if s[0] == s[1] and s[1] == s[2] and s[2] == s[3]:
        print("Weak")
    else:
        if (int(s[0]) + 1) % 10 == int(s[1]) and (int(s[1]) + 1) % 10 == int(s[2]) and (int(s[2]) + 1) % 10 == int(s[3]):
            print("Weak")
        else:
            print("Strong")

=======
Suggestion 4

def main():
    X = input()
    if X[0] == X[1] == X[2] == X[3]:
        print("Weak")
    elif (int(X[0])+1)%10 == int(X[1]) and (int(X[1])+1)%10 == int(X[2]) and (int(X[2])+1)%10 == int(X[3]):
        print("Weak")
    else:
        print("Strong")

=======
Suggestion 5

def main():
    a = input()
    if a[0] == a[1] and a[1] == a[2] and a[2] == a[3]:
        print('Weak')
    elif (int(a[0])+1)%10 == int(a[1]) and (int(a[1])+1)%10 == int(a[2]) and (int(a[2])+1)%10 == int(a[3]):
        print('Weak')
    else:
        print('Strong')

=======
Suggestion 6

def main():
    # input
    X = input()
    # compute
    if X[0] == X[1] and X[1] == X[2] and X[2] == X[3]:
        print("Weak")
    elif (int(X[0])+1)%10 == int(X[1]) and (int(X[1])+1)%10 == int(X[2]) and (int(X[2])+1)%10 == int(X[3]):
        print("Weak")
    else:
        print("Strong")
    # output

=======
Suggestion 7

def main():
    X = input()
    if X == X[0]*4 or X in ['0123','1234','2345','3456','4567','5678','6789','7890','8901','9012']:
        print('Weak')
    else:
        print('Strong')

=======
Suggestion 8

def main():
    password = list(input())
    if password[0] == password[1] and password[1] == password[2] and password[2] == password[3]:
        print('Weak')
    else:
        if password[0] == '9' and password[1] == '0' and password[2] == '1' and password[3] == '2':
            print('Weak')
        else:
            if int(password[1]) == (int(password[0]) + 1) % 10 and int(password[2]) == (int(password[1]) + 1) % 10 and int(password[3]) == (int(password[2]) + 1) % 10:
                print('Weak')
            else:
                print('Strong')

=======
Suggestion 9

def is_weak(x):
    if x[0] == x[1] == x[2] == x[3]:
        return True
    if int(x[0]) == int(x[1]) + 1 and int(x[1]) == int(x[2]) + 1 and int(x[2]) == int(x[3]) + 1:
        return True
    if int(x[0]) == 0 and int(x[1]) == 9 and int(x[2]) == 8 and int(x[3]) == 9:
        return True
    return False

=======
Suggestion 10

def main():
    # input
    X = input()
    
    # compute
    if ((X[0]==X[1]==X[2]==X[3]) or (int(X[0])==int(X[1])-1==int(X[2])-2==int(X[3])-3) or (int(X[0])==9 and int(X[1])==0 and int(X[2])==1 and int(X[3])==2)):
        ans = 'Weak'
    else:
        ans = 'Strong'
    
    # output
    print(ans)
