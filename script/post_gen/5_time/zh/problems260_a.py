Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    if s[0] == s[1]:
        print(s[2])
    elif s[1] == s[2]:
        print(s[0])
    elif s[0] == s[2]:
        print(s[1])
    else:
        print(-1)

=======
Suggestion 2

def solution(s):
    if s[0] == s[1] and s[1] == s[2]:
        return -1
    elif s[0] == s[1]:
        return s[2]
    elif s[1] == s[2]:
        return s[0]
    elif s[0] == s[2]:
        return s[1]
    else:
        return -1

=======
Suggestion 3

def solve(string):
    for i in string:
        if string.count(i) == 1:
            return i
    return -1

=======
Suggestion 4

def main():
    S = input()
    if S[0] == S[1] and S[1] == S[2]:
        print(-1)
    elif S[0] != S[1] and S[1] == S[2]:
        print(S[0])
    elif S[0] == S[1] and S[1] != S[2]:
        print(S[2])
    elif S[0] != S[1] and S[1] != S[2] and S[0] == S[2]:
        print(S[1])
    else:
        print(-1)

=======
Suggestion 5

def main():
    S = input()
    if S[0] != S[1] and S[1] != S[2] and S[0] != S[2]:
        print("1")
    elif S[0] == S[1] and S[1] != S[2]:
        print("2")
    elif S[0] != S[1] and S[1] == S[2]:
        print("3")
    else:
        print("-1")

=======
Suggestion 6

def solve():
    s = input()
    if s[0] != s[1] and s[1] != s[2] and s[2] != s[0]:
        print(-1)
    elif s[0] == s[1]:
        print(s[2])
    elif s[1] == s[2]:
        print(s[0])
    else:
        print(s[1])

=======
Suggestion 7

def solve():
    s = input()
    if s[0] != s[1] and s[1] != s[2] and s[2] != s[0]:
        print(s[0])
    elif s[0] == s[1] and s[1] != s[2]:
        print(s[2])
    elif s[1] == s[2] and s[2] != s[0]:
        print(s[0])
    elif s[2] == s[0] and s[0] != s[1]:
        print(s[1])
    else:
        print(-1)

=======
Suggestion 8

def main():
    s = input()
    if s[0] == s[1] and s[1] != s[2]:
        print(s[2])
    elif s[0] == s[2] and s[1] != s[2]:
        print(s[1])
    elif s[1] == s[2] and s[0] != s[1]:
        print(s[0])
    else:
        print(-1)

=======
Suggestion 9

def main():
    s = input()
    if s[0] == s[1]:
        print(s[2])
    elif s[0] == s[2]:
        print(s[1])
    elif s[1] == s[2]:
        print(s[0])
    else:
        print(-1)

=======
Suggestion 10

def getUniqueChar(s):
    if s[0] == s[1]:
        return s[2]
    if s[1] == s[2]:
        return s[0]
    if s[0] == s[2]:
        return s[1]
    return -1
