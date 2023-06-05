Synthesizing 10/10 solutions

=======
Suggestion 1

def check(s1,s2):
    if s1[0][0] == '#' and s1[0][1] == '#' and s1[1][0] == '#' and s1[1][1] == '#':
        return 'Yes'
    elif s2[0][0] == '#' and s2[0][1] == '#' and s2[1][0] == '#' and s2[1][1] == '#':
        return 'Yes'
    else:
        return 'No'

=======
Suggestion 2

def main():
    s1 = input()
    s2 = input()
    if s1[1] == '#' and s2[1] == '#' or s1[1] == '#' and s2[0] == '#' or s1[0] == '#' and s2[1] == '#' or s1[0] == '#' and s2[0] == '#':
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    s1 = input()
    s2 = input()
    if s1[0] == '#' and s1[1] == '#' and s2[0] == '#' and s2[1] == '#':
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def check(s1, s2):
    if s1[0] == '#' and s1[1] == '#' and s2[0] == '#' and s2[1] == '#':
        return True
    else:
        return False

s1 = input()
s2 = input()

=======
Suggestion 5

def solve():
    s1 = input()
    s2 = input()
    if s1[1] == '#' and s2[1] == '#' and s1[0] == '#' and s2[0] == '#':
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    S_1 = input()
    S_2 = input()
    if S_1[1] == '#' and S_2[0] == '#':
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    #输入
    S_1 = input()
    S_2 = input()

    #处理
    if S_1[0] == '#' and S_1[1] == '#' and S_2[0] == '#' and S_2[1] == '#':
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def solution():
    s1 = input()
    s2 = input()
    if s1[0] == '#' and s1[1] == '#' and s2[0] == '#' and s2[1] == '#':
        print('Yes')
    else:
        print('No')

solution()

=======
Suggestion 9

def main():
    s1 = input()
    s2 = input()
    if s1[0] == "#" and s1[1] == "#" and s2[0] == "#" and s2[1] == "#":
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def problem229_a():
    s1 = input()
    s2 = input()
    if s1[0] == '#' and s1[1] == '#' and s2[0] == '#' and s2[1] == '#':
        print('Yes')
    elif s1[0] == '#' and s1[1] == '#' and s2[0] == '#' and s2[1] == '.':
        print('Yes')
    elif s1[0] == '#' and s1[1] == '#' and s2[0] == '.' and s2[1] == '#':
        print('Yes')
    elif s1[0] == '#' and s1[1] == '.' and s2[0] == '#' and s2[1] == '#':
        print('Yes')
    elif s1[0] == '#' and s1[1] == '.' and s2[0] == '#' and s2[1] == '.':
        print('Yes')
    elif s1[0] == '.' and s1[1] == '#' and s2[0] == '#' and s2[1] == '#':
        print('Yes')
    elif s1[0] == '.' and s1[1] == '#' and s2[0] == '#' and s2[1] == '.':
        print('Yes')
    elif s1[0] == '.' and s1[1] == '#' and s2[0] == '.' and s2[1] == '#':
        print('Yes')
    elif s1[0] == '.' and s1[1] == '.' and s2[0] == '#' and s2[1] == '#':
        print('Yes')
    elif s1[0] == '#' and s1[1] == '.' and s2[0] == '.' and s2[1] == '.':
        print('Yes')
    elif s1[0] == '.' and s1[1] == '#' and s2[0] == '.' and s2[1] == '.':
        print('Yes')
    elif s1[0] == '.' and s1[1] == '.' and s2[0] == '#' and s2[1] == '.':
        print('Yes')
    elif s1[0] == '.' and s1[1] ==
