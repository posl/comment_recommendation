Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    t = input()
    if t.startswith(s):
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    s = input()
    t = input()
    if s == t[:len(s)]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    s = input()
    t = input()
    if t.startswith(s):
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    s = input()
    t = input()
    if s == t[0:len(s)]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    S = input()
    T = input()
    if T.startswith(S):
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    s = input()
    t = input()
    if t[:len(s)] == s:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    s = input()
    t = input()

    if s == t[:len(s)]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def is_prefix(str1, str2):
    if str1 == str2[:len(str1)]:
        return True
    else:
        return False
