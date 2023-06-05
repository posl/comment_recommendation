Synthesizing 10/10 solutions

=======
Suggestion 1

def single_char(s):
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            return s[i]
    return -1

=======
Suggestion 2

def find_unique_char(s):
    if s[0] != s[1] and s[0] != s[2]:
        return s[0]
    elif s[1] != s[0] and s[1] != s[2]:
        return s[1]
    elif s[2] != s[0] and s[2] != s[1]:
        return s[2]
    else:
        return -1

=======
Suggestion 3

def findchar(s):
    if s[0] != s[1] and s[0] != s[2]:
        print(s[0])
    elif s[1] != s[0] and s[1] != s[2]:
        print(s[1])
    elif s[2] != s[0] and s[2] != s[1]:
        print(s[2])
    else:
        print(-1)

=======
Suggestion 4

def main():
    s = input()
    s = list(s)
    for i in range(3):
        if s.count(s[i]) == 1:
            print(s[i])
            return
    print(-1)

=======
Suggestion 5

def main():
    s = input()
    if s[0] == s[1] and s[1] == s[2]:
        print("-1")
    elif s[0] == s[1]:
        print(s[2])
    elif s[1] == s[2]:
        print(s[0])
    elif s[2] == s[0]:
        print(s[1])
    else:
        print("-1")
main()

=======
Suggestion 6

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
Suggestion 7

def solve():
    # 编写从这里开始
    s = input()
    if s[0] == s[1] == s[2]:
        print(-1)
    elif s[0] == s[1]:
        print(s[2])
    elif s[0] == s[2]:
        print(s[1])
    elif s[1] == s[2]:
        print(s[0])
    else:
        print(s[0])

=======
Suggestion 8

def find_unique_char(s):
    if s[0] != s[1] and s[1] != s[2] and s[0] != s[2]:
        return s[0]
    elif s[0] == s[1] and s[1] != s[2]:
        return s[2]
    elif s[0] != s[1] and s[1] == s[2]:
        return s[0]
    elif s[0] == s[1] and s[1] == s[2]:
        return -1

=======
Suggestion 9

def solve(s):
    if s[0] == s[1]:
        return s[2]
    elif s[0] == s[2]:
        return s[1]
    elif s[1] == s[2]:
        return s[0]
    else:
        return -1

=======
Suggestion 10

def main():
    S = input()
    if S[0] == S[1] and S[0] != S[2]:
        print(S[2])
    elif S[0] != S[1] and S[0] == S[2]:
        print(S[1])
    elif S[0] != S[1] and S[1] == S[2]:
        print(S[0])
    else:
        print(-1)
