Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    t = input()
    if s + 'a' == t:
        print('Yes')
    elif s + 'z' == t:
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
    S = input()
    T = input()
    if S == T[:-1]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    S = input()
    T = input()
    if S + 'a' == T:
        print('Yes')
    elif S + 'z' == T:
        print('Yes')
    elif S + 'zz' == T:
        print('Yes')
    elif S + 'zzz' == T:
        print('Yes')
    elif S + 'zzzz' == T:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    S = input()
    T = input()
    if S + "z" == T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    s = input()
    t = input()
    if t == s + "z":
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    S = input()
    T = input()

    if S == T[:-1]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def is_same(s1, s2):
    if len(s1) != len(s2) - 1:
        return False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True

=======
Suggestion 9

def solve():
    S = input()
    T = input()
    if S == T[:-1]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 10

def main():
    S = input()
    T = input()
    if len(S) == len(T) - 1:
        if S == T[:-1]:
            print("Yes")
            return
    print("No")
