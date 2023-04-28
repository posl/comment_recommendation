Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 2

def main():
    S = input()
    if S[0] != S[1] and S[0] != S[2]:
        print(S[0])
    elif S[1] != S[0] and S[1] != S[2]:
        print(S[1])
    elif S[2] != S[0] and S[2] != S[1]:
        print(S[2])
    else:
        print(-1)

=======
Suggestion 3

def solve():
    s = input()
    if s[0] == s[1] and s[0] == s[2]:
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
Suggestion 4

def main():
    str = input()
    print(str[0] if str[0] != str[1] and str[0] != str[2] else str[1] if str[1] != str[0] and str[1] != str[2] else str[2] if str[2] != str[0] and str[2] != str[1] else -1)

=======
Suggestion 5

def main():
    s = input()
    if s[0] == s[1] == s[2]:
        print(-1)
    else:
        print(s[0])

=======
Suggestion 6

def main():
    S = input()
    S_list = list(S)

    for s in S_list:
        if S_list.count(s) == 1:
            print(s)
            exit()
    print(-1)

=======
Suggestion 7

def problem():
    S = input()
    S = list(S)
    for i in range(0, len(S)):
        if S.count(S[i]) == 1:
            print(S[i])
            return
    print(-1)

problem()

=======
Suggestion 8

def main():
    # S = input().rstrip()
    S = input().rstrip()
    # print(S)
    # print(len(S))
    # print(S[0])
    # print(S[1])
    # print(S[2])
    # print(S[0] == S[1])
    # print(S[0] == S[2])
    # print(S[1] == S[2])
    if S[0] == S[1]:
        print(S[2])
    elif S[0] == S[2]:
        print(S[1])
    elif S[1] == S[2]:
        print(S[0])
    else:
        print('-1')

=======
Suggestion 9

def get_input():
    return input()
