Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    T = input()
    if S + 'a' == T:
        print('Yes')
    elif S + 'b' == T:
        print('Yes')
    elif S + 'c' == T:
        print('Yes')
    elif S + 'd' == T:
        print('Yes')
    elif S + 'e' == T:
        print('Yes')
    elif S + 'f' == T:
        print('Yes')
    elif S + 'g' == T:
        print('Yes')
    elif S + 'h' == T:
        print('Yes')
    elif S + 'i' == T:
        print('Yes')
    elif S + 'j' == T:
        print('Yes')
    elif S + 'k' == T:
        print('Yes')
    elif S + 'l' == T:
        print('Yes')
    elif S + 'm' == T:
        print('Yes')
    elif S + 'n' == T:
        print('Yes')
    elif S + 'o' == T:
        print('Yes')
    elif S + 'p' == T:
        print('Yes')
    elif S + 'q' == T:
        print('Yes')
    elif S + 'r' == T:
        print('Yes')
    elif S + 's' == T:
        print('Yes')
    elif S + 't' == T:
        print('Yes')
    elif S + 'u' == T:
        print('Yes')
    elif S + 'v' == T:
        print('Yes')
    elif S + 'w' == T:
        print('Yes')
    elif S + 'x' == T:
        print('Yes')
    elif S + 'y' == T:
        print('Yes')
    elif S + 'z' == T:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    s = input()
    t = input()
    if s == t[:-1]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    s = input()
    t = input()
    if s == t[:-1]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    S = input()
    T = input()
    if S == T[:-1]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    s = input()
    t = input()
    if t == s + "z":
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    S = input()
    T = input()
    if len(S) == (len(T) - 1):
        if S == T[0:len(S)]:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

=======
Suggestion 7

def check(s, t):
    if len(s) + 1 == len(t):
        if s == t[:-1]:
            return True
    return False
