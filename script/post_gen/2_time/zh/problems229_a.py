Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s1 = input()
    s2 = input()
    if s1[0] == "#" and s1[1] == "#" and s2[0] == "#" and s2[1] == "#":
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    s1 = input()
    s2 = input()
    if s1[0] == '#' and s1[1] == '#' and s2[0] == '#' and s2[1] == '#':
        print('Yes')
    elif s1[0] == '#' and s1[1] == '#' and s2[0] == '#' and s2[1] == '.':
        print('Yes')
    elif s1[0] == '#' and s1[1] == '#' and s2[0] == '.' and s2[1] == '#':
        print('Yes')
    elif s1[0] == '#' and s1[1] == '#' and s2[0] == '.' and s2[1] == '.':
        print('Yes')
    elif s1[0] == '#' and s1[1] == '.' and s2[0] == '#' and s2[1] == '#':
        print('Yes')
    elif s1[0] == '#' and s1[1] == '.' and s2[0] == '#' and s2[1] == '.':
        print('Yes')
    elif s1[0] == '#' and s1[1] == '.' and s2[0] == '.' and s2[1] == '#':
        print('Yes')
    elif s1[0] == '#' and s1[1] == '.' and s2[0] == '.' and s2[1] == '.':
        print('Yes')
    elif s1[0] == '.' and s1[1] == '#' and s2[0] == '#' and s2[1] == '#':
        print('Yes')
    elif s1[0] == '.' and s1[1] == '#' and s2[0] == '#' and s2[1] == '.':
        print('Yes')
    elif s1[0] == '.' and s1[1] == '#' and s2[0] == '.' and s2[1] == '#':
        print('Yes')
    elif s1[0] == '.' and s1[1] == '#' and s2[0] == '.' and s2[1] == '.':
        print('Yes')
    elif s1[0] == '.' and s1[1] == '.' and

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

def main():
    s1 = input()
    s2 = input()
    if s1[0] == '#' and s2[0] == '#':
        print('Yes')
    elif s1[0] == '#' and s2[0] == '.':
        if s1[1] == '#':
            print('Yes')
        else:
            print('No')
    elif s1[0] == '.' and s2[0] == '#':
        if s2[1] == '#':
            print('Yes')
        else:
            print('No')
    else:
        print('No')

=======
Suggestion 5

def solve():
    s1 = input()
    s2 = input()
    if s1[0] == '#' and s1[1] == '#' and s2[0] == '#' and s2[1] == '#':
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    S1 = input()
    S2 = input()
    if S1[0] == '#' and S1[1] == '#' and S2[0] == '#' and S2[1] == '#':
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    S_1 = input()
    S_2 = input()
    if S_1[0] == '#' and S_1[1] == '#' and S_2[0] == '#' and S_2[1] == '#':
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    s1 = input()
    s2 = input()
    if (s1[0] == '#' and s1[1] == '#' and s2[0] == '#' and s2[1] == '#') or (s1[0] == '#' and s1[1] == '.' and s2[0] == '#' and s2[1] == '#') or (s1[0] == '#' and s1[1] == '#' and s2[0] == '#' and s2[1] == '.') or (s1[0] == '.' and s1[1] == '#' and s2[0] == '#' and s2[1] == '#') or (s1[0] == '#' and s1[1] == '#' and s2[0] == '.' and s2[1] == '#') or (s1[0] == '#' and s1[1] == '#' and s2[0] == '#' and s2[1] == '#'):
        print('Yes')
    else:
        print('No')
