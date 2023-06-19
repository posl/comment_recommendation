Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    T = input()
    if S == T[:-1]:
        print("Yes")
    else:
        print("No")

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
    if len(S) == len(T) - 1:
        if S == T[:-1]:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

=======
Suggestion 4

def main():
    s = input()
    t = input()
    if len(s)+1 == len(t):
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    s = input()
    t = input()
    if s == t[:-1]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    S = input()
    T = input()
    if T == S + "z":
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def check(s, t):
    if not len(s) + 1 == len(t):
        return False
    if not t.startswith(s):
        return False
    return True

s = input()
t = input()

=======
Suggestion 8

def input():
    s = raw_input()
    t = raw_input()
    return s, t
