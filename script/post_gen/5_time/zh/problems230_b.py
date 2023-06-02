Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    if S.count('o') > 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    s = input()
    if "o" in s:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    S = input()
    if S.count('o') == 2:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def problem230_b():
    s = input()
    if s.count('o') >= 1 and s.count('x') >= 1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    s = input()
    if s.count('o') == 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    S = input()
    if S in 'xoxoxoxoxo':
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    s = input()
    t = "x" * 100000
    if s in t:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    s = input()
    if "o" in s and "x" in s:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    s = input()
    if s.find("o") > -1 and s.find("x") > -1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    S = input()
    if S[0] == 'o' or S[1] == 'o' or S[2] == 'o':
        print('Yes')
    else:
        print('No')
