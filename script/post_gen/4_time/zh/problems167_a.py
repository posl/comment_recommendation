Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    t = input()
    if len(t) - len(s) == 1 and t[:len(s)] == s:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    s = input()
    t = input()
    if t == s + 'z':
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    s = input()
    t = input()
    if s + "z" == t:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    s = input()
    t = input()
    if s == t[:-1]:
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
    if len(S) + 1 == len(T):
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    s = raw_input()
    t = raw_input()
    if s + t[-1] == t:
        print "Yes"
    else:
        print "No"

=======
Suggestion 8

def main():
    s = input()
    t = input()
    if (t == s + "z"):
        print("Yes")
    else:
        print("No")
