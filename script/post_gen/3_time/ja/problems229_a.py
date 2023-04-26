Synthesizing 10/10 solutions (Duplicates hidden)

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
        print("No")
    else:
        print("Yes")

=======
Suggestion 3

def main():
    s1 = input()
    s2 = input()
    if s1[0] == '#' and s1[1] == '#':
        print('Yes')
    elif s2[0] == '#' and s2[1] == '#':
        print('Yes')
    else:
        print('No')
    return

=======
Suggestion 4

def main():
    S1 = input()
    S2 = input()
    if S1[0] == '#' and S1[1] == '#' and S2[0] == '#' and S2[1] == '#':
        print('Yes')
    else:
        print('No')
main()

=======
Suggestion 5

def main():
    s1 = input()
    s2 = input()
    if s1[0] == '#' and s1[1] == '#' or s2[0] == '#' and s2[1] == '#':
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def solve():
    s1 = input()
    s2 = input()
    if s1[0] == '#' and s1[1] == '#':
        print("Yes")
    elif s2[0] == '#' and s2[1] == '#':
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    s1 = input()
    s2 = input()

    if s1[0] == s2[0] and s1[1] == s2[1]:
        print('No')
    else:
        print('Yes')

=======
Suggestion 8

def main():
    S = [input() for i in range(2)]
    if S[0][0] == '#' and S[1][0] == '#' or S[0][1] == '#' and S[1][1] == '#' or S[0][0] == '#' and S[0][1] == '#' or S[1][0] == '#' and S[1][1] == '#':
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    s1 = input()
    s2 = input()
    if s1 == ".." or s2 == "..":
        print("No")
    else:
        print("Yes")
