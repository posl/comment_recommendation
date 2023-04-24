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
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    s = input()
    t = input()
    if t[:-1] == s:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    s = input()
    t = input()
    if t[:-1] == s:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    s = input()
    t = input()
    if t[:len(s)] == s:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    S = input()
    T = input()
    if T.startswith(S) and len(T) == len(S) + 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    s = input()
    t = input()

    if t[0:len(s)] == s:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    s = input()
    t = input()
    if s == t[0:len(s)]:
        print('Yes')
    else:
        print('No')
