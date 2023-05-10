Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def weak_or_strong(num):
    if num[0] == num[1] and num[1] == num[2] and num[2] == num[3]:
        return "Weak"
    elif num[0] == "9" and num[1] == "8" and num[2] == "7" and num[3] == "6":
        return "Weak"
    elif int(num[0]) == int(num[1]) - 1 and int(num[1]) == int(num[2]) - 1 and int(num[2]) == int(num[3]) - 1:
        return "Weak"
    else:
        return "Strong"

=======
Suggestion 2

def main():
    X = input()
    if X[0] == X[1] == X[2] == X[3]:
        print("Weak")
    elif (int(X[0])+1)%10 == int(X[1]) and (int(X[1])+1)%10 == int(X[2]) and (int(X[2])+1)%10 == int(X[3]):
        print("Weak")
    else:
        print("Strong")

=======
Suggestion 3

def main():
    x = input()
    if x[0] == x[1] == x[2] == x[3]:
        print("Weak")
    elif (int(x[0])+1)%10 == int(x[1]) and (int(x[1])+1)%10 == int(x[2]) and (int(x[2])+1)%10 == int(x[3]):
        print("Weak")
    else:
        print("Strong")

=======
Suggestion 4

def main():
    X = input()
    if X == X[0]*4:
        print("Weak")
        return
    for i in range(3):
        if int(X[i]) == 9:
            if int(X[i+1]) != 0:
                print("Strong")
                return
        else:
            if int(X[i+1]) != int(X[i])+1:
                print("Strong")
                return
    print("Weak")

=======
Suggestion 5

def main():
    N = input()
    if N[0] == N[1] == N[2] == N[3]:
        print("Weak")
    else:
        if (int(N[0])+1)%10 == int(N[1]) and (int(N[1])+1)%10 == int(N[2]) and (int(N[2])+1)%10 == int(N[3]):
            print("Weak")
        else:
            print("Strong")

=======
Suggestion 6

def main():
    s = input()
    if s[0] == s[1] and s[1] == s[2] and s[2] == s[3]:
        print("Weak")
    else:
        if int(s[0]) == 9 and int(s[1]) == 0 and int(s[2]) == 1 and int(s[3]) == 2:
            print("Weak")
        else:
            if (int(s[1]) - int(s[0]) + 10) % 10 == 1 and (int(s[2]) - int(s[1]) + 10) % 10 == 1 and (int(s[3]) - int(s[2]) + 10) % 10 == 1:
                print("Weak")
            else:
                print("Strong")

=======
Suggestion 7

def is_weak_password(x):
    if x[0] == x[1] and x[1] == x[2] and x[2] == x[3]:
        return True
    elif (x[0] + 1) % 10 == x[1] and (x[1] + 1) % 10 == x[2] and (x[2] + 1) % 10 == x[3]:
        return True
    else:
        return False

=======
Suggestion 8

def main():
    #input
    x = input()
    #output
    if x[0]==x[1]==x[2]==x[3] or \
        x[1]==str((int(x[0])+1)%10) and x[2]==str((int(x[1])+1)%10) and x[3]==str((int(x[2])+1)%10):
        print("Weak")
    else:
        print("Strong")

=======
Suggestion 9

def main():
    x = input()
    if x[0] == x[1] and x[1] == x[2] and x[2] == x[3]:
        print("Weak")
        return
    for i in range(3):
        if int(x[i+1]) != (int(x[i])+1)%10:
            print("Strong")
            return
    print("Weak")
