Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s = input()
    print(s.replace("na", "nya"))

=======
Suggestion 2

def solve():
    n = int(input())
    s = input()
    s = s.replace('na', 'nya')
    print(s)

=======
Suggestion 3

def problem():
    n = int(input())
    s = input()
    print(s.replace('na', 'nya'))

=======
Suggestion 4

def replace_na(s):
    if len(s) < 2:
        return s
    else:
        if s[0:2] == 'na':
            return 'nya' + replace_na(s[2:])
        else:
            return s[0] + replace_na(s[1:])

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    s = s.replace("na", "nya")
    print(s)

=======
Suggestion 6

def replace_na(s):
    s = s.replace('na', 'nya')
    return s

=======
Suggestion 7

def replace_na(s):
    return s.replace('na', 'nya')

=======
Suggestion 8

def main():
    N = int(input())
    S = input()
    print(S.replace('na', 'nya'))
