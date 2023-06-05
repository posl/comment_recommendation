Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(S, T):
    if T == S + 'z':
        return 'Yes'
    else:
        return 'No'

=======
Suggestion 2

def func(s,t):
    if len(s) + 1 != len(t):
        return False
    if s + t[-1] == t:
        return True
    else:
        return False

=======
Suggestion 3

def main():
    s = input()
    t = input()
    if t == s + 'z':
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def check(s, t):
    if len(t) != len(s) + 1:
        return False
    if s == t[:-1]:
        return True
    return False

=======
Suggestion 5

def main():
    s = input()
    t = input()
    if s == t[:-1]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def solve():
    s = input()
    t = input()
    if t == s + 'z':
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    S = input()
    T = input()
    if T == S + "z":
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    S = input()
    T = input()
    if S == T[:-1]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    S = input()
    T = input()
    if T == S + 'z':
        print('Yes')
    else:
        print('No')

=======
Suggestion 10

def main():
    S = input()
    T = input()
    if (len(S) == 1 and len(T) == 2):
        print("Yes")
    elif (len(S) == 1 and len(T) == 1):
        print("No")
    elif (len(S) == len(T) - 1):
        if (S == T[0:-1]):
            print("Yes")
        else:
            print("No")
    else:
        print("No")
