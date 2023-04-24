Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s1 = input()
    s2 = input()
    if s1[0] == '#' or s1[1] == '#' or s2[0] == '#' or s2[1] == '#':
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    s1 = input()
    s2 = input()
    if s1[0] == '#' and s1[1] == '#' and s2[0] == '#' and s2[1] == '#':
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    S1 = input()
    S2 = input()
    if (S1[0] == '#' or S1[1] == '#') and (S2[0] == '#' or S2[1] == '#'):
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    S1 = input()
    S2 = input()
    if S1[0] == '#' and S1[1] == '#' and S2[0] == '#' and S2[1] == '#':
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    s1 = input()
    s2 = input()
    if s1[0] == '#' and s1[1] == '#' or s2[0] == '#' and s2[1] == '#' or s1[1] == '#' and s2[0] == '#' or s1[0] == '#' and s2[1] == '#':
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def solve():
    s1 = input()
    s2 = input()
    if s1[0] == '#' or s1[1] == '#' or s2[0] == '#' or s2[1] == '#':
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    s1 = input()
    s2 = input()

    if "#" in s1[0] and "#" in s1[1] and "#" in s2[0] and "#" in s2[1]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def solve():
    S1 = input()
    S2 = input()
    if '#' in S1[0] and '#' in S2[0]:
        print('Yes')
    elif '#' in S1[1] and '#' in S2[1]:
        print('Yes')
    else:
        print('No')

solve()

=======
Suggestion 9

def main():
    # S_1 = input()
    # S_2 = input()
    # S_1 = "###"
    # S_2 = ".#."
    S_1 = ".#."
    S_2 = "##."
    if (S_1[0] == "#" or S_1[1] == "#") and (S_2[0] == "#" or S_2[1] == "#"):
        print("Yes")
    else:
        print("No")
