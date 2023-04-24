Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S1 = input()
    S2 = input()
    if S1[0] == S2[0] and S1[1] == S2[1] and S1[2] == S2[2]:
        print("No")
    else:
        print("Yes")

=======
Suggestion 2

def main():
    s1 = input()
    s2 = input()
    if s1[0] == s1[1] == s2[0] == s2[1] == ".":
        print("No")
    else:
        print("Yes")

=======
Suggestion 3

def main():
    s1 = input()
    s2 = input()
    if s1[0] == s1[1] == s2[0] == s2[1] == "#":
        print("No")
    else:
        print("Yes")

=======
Suggestion 4

def main():
    S1 = input()
    S2 = input()
    if S1[0] == "#" and S1[1] == "#":
        print("Yes")
    elif S2[0] == "#" and S2[1] == "#":
        print("Yes")
    elif S1[0] == "#" and S2[1] == "#":
        print("Yes")
    elif S1[1] == "#" and S2[0] == "#":
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    s1 = input()
    s2 = input()
    if s1[0] == s2[0] and s1[1] == s2[1]:
        print("No")
    else:
        print("Yes")

=======
Suggestion 6

def main():
    S1 = input()
    S2 = input()
    if S1[0] == S1[1] == S2[0] == S2[1] == '.':
        print('No')
    else:
        print('Yes')

=======
Suggestion 7

def main():
    s1 = input()
    s2 = input()
    if s1[0] == s1[1] == s2[0] == s2[1] == '#':
        print('No')
    else:
        print('Yes')

=======
Suggestion 8

def main():
    S1 = input()
    S2 = input()

    if S1[0] == S1[1] == S2[0] == S2[1] == '#':
        print('No')
    else:
        print('Yes')

=======
Suggestion 9

def main():
    S = [input() for _ in range(2)]
    if S[0][0] == S[0][1] == S[1][0] == S[1][1] == '.':
        print('No')
    else:
        print('Yes')
