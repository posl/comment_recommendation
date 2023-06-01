Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    if 'o' in s and 'x' in s:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    s = input()
    if s.count('o') == 0:
        print('No')
    else:
        print('Yes')

=======
Suggestion 3

def main():
    s = input()
    if 'o' in s:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def isSubString(T, S):
    index = 0
    for t in T:
        if t == S[index]:
            index += 1
        if index == len(S):
            return True
    return False

=======
Suggestion 5

def main():
    s = input()
    if s == "ox" or s == "xo":
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    s = input()
    if s == 'ox' or s == 'xo':
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def solve():
    S = input()
    T = 'x' * 10**5
    if S in T:
        print('Yes')
    else:
        print('No')
solve()

=======
Suggestion 8

def main():
    s = input()
    if len(s) == 2:
        if s[0] == 'o' or s[1] == 'o':
            print('Yes')
        else:
            print('No')
    else:
        print('Yes')

=======
Suggestion 9

def solve():
    S = input()
    if S.find("oo") != -1:
        print("Yes")
    elif S.find("xx") != -1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def get_input():
    return input()
