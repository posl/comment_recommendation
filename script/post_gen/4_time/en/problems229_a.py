Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s1 = input()
    s2 = input()
    if '#' in s1[0] and '#' in s1[1] and '#' in s2[0] and '#' in s2[1]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def problems229_a():
    s1 = input()
    s2 = input()
    if s1[0] == '#' and s1[1] == '#' and s2[0] == '#' and s2[1] == '#':
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def solve():
    s1 = input()
    s2 = input()
    if "#" in [s1[0], s1[1], s2[0], s2[1]]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    S_1 = input()
    S_2 = input()
    if '#' in S_1 and '#' in S_2:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    S_1 = input()
    S_2 = input()
    if S_1[0] == '#' and S_1[1] == '#' or S_2[0] == '#' and S_2[1] == '#':
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    s1 = input()
    s2 = input()

    if '#' in s1 and '#' in s2:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    S_1 = input()
    S_2 = input()
    if S_1[1] == '#' or S_2[0] == '#':
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    s1 = input()
    s2 = input()
    if s1[1] == s2[1] == '#':
        print('Yes')
    elif s1[0] == s2[0] == '#':
        print('Yes')
    elif s1[0] == s2[1] == '#':
        print('Yes')
    elif s1[1] == s2[0] == '#':
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def is_possible(s1, s2):
    if s1[0] == '#' and s1[1] == '#':
        return 'Yes'
    elif s2[0] == '#' and s2[1] == '#':
        return 'Yes'
    elif s1[0] == '#' and s2[0] == '#':
        return 'Yes'
    elif s1[1] == '#' and s2[1] == '#':
        return 'Yes'
    else:
        return 'No'

=======
Suggestion 10

def check_grid(s1, s2):
    if s1[0] == '#' and s1[1] == '#' and s2[0] == '#' and s2[1] == '#':
        return 'Yes'
    return 'No'
