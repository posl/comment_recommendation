Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    if len(set(s)) == 2 and s.count(s[0]) == 2:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    s = input()
    if len(set(s)) == 2 and s.count(s[0]) == 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    S = input()
    if len(set(S)) == 2 and S.count(S[0]) == 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def solve():
    S = input()
    S = sorted(S)
    if S[0] == S[1] and S[2] == S[3] and S[0] != S[2]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def check(s):
    l = list(s)
    l.sort()
    if l[0] == l[1] and l[2] == l[3] and l[0] != l[2]:
        return True
    else:
        return False

s = input()

=======
Suggestion 6

def main():
    S = input()
    S_set = set(S)
    if len(S_set) == 2:
        print('Yes')
    else:
        print('No')
