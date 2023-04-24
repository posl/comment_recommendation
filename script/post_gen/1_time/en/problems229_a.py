Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s1 = input()
    s2 = input()
    if s1[0] == '#' and s1[1] == '#' and s2[0] == '#' and s2[1] == '#':
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    s1 = input()
    s2 = input()
    if s1[0] == "#" and s1[1] == "#" and s2[0] == "#" and s2[1] == "#":
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    s1 = input()
    s2 = input()
    if "#" in s1[0] and "#" in s1[1] and "#" in s2[0] and "#" in s2[1]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    S_1 = input()
    S_2 = input()
    if S_1[0] == '#' and S_1[1] == '#' and S_2[0] == '#' and S_2[1] == '#':
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    s1 = input()
    s2 = input()
    if s1[0] == '#' and s1[1] == '#':
        print('Yes')
    elif s2[0] == '#' and s2[1] == '#':
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    S1 = input()
    S2 = input()

    if '#' in [S1[0], S1[1], S2[0], S2[1]]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    s1 = input()
    s2 = input()
    if "#" in s1 and "#" in s2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def solve():
    s1 = input()
    s2 = input()
    if s1[0] == '#' and s1[1] == '#' or s2[0] == '#' and s2[1] == '#':
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    s1 = input()
    s2 = input()
    print('Yes' if s1[1] == s2[0] and s1[2] == s2[1] and s1[0] == s2[2] else 'No')

=======
Suggestion 10

def main():
    s1 = input()
    s2 = input()
    if s1[1] == s2[1]:
        print("Yes")
    else:
        print("No")
