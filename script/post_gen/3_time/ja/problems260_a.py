Synthesizing 10/10 solutions

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
    if S[0] == S[1]:
        print(S[2])
    elif S[0] == S[2]:
        print(S[1])
    elif S[1] == S[2]:
        print(S[0])
    else:
        print(-1)

=======
Suggestion 3

def main():
    s = input()
    if s[0] == s[1] and s[1] != s[2]:
        print(s[2])
    elif s[0] == s[2] and s[1] != s[2]:
        print(s[1])
    elif s[1] == s[2] and s[0] != s[2]:
        print(s[0])
    else:
        print(-1)

=======
Suggestion 4

def main():
    s = input()
    if s[0] == s[1] and s[1] == s[2]:
        print(-1)
    elif s[0] == s[1]:
        print(s[2])
    elif s[1] == s[2]:
        print(s[0])
    elif s[0] == s[2]:
        print(s[1])
    else:
        print(s[0])

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
    elif s[0] == s[2]:
        print(s[1])
    else:
        print("-1")

=======
Suggestion 6

def main():
    s = input()
    if s[0] == s[1] and s[1] == s[2]:
        print('-1')
    elif s[0] == s[1]:
        print(s[2])
    elif s[1] == s[2]:
        print(s[0])
    elif s[0] == s[2]:
        print(s[1])
    else:
        print(s[0])

=======
Suggestion 7

def main():
    s = input()
    if s[0] == s[1] and s[0] == s[2]:
        print("-1")
    elif s[0] == s[1]:
        print(s[2])
    elif s[0] == s[2]:
        print(s[1])
    elif s[1] == s[2]:
        print(s[0])
    else:
        print("-1")

=======
Suggestion 8

def main():
    # input
    S = input()

    # compute

    # output
    if S[0] == S[1] == S[2]:
        print(-1)
    elif S[0] == S[1]:
        print(S[2])
    elif S[1] == S[2]:
        print(S[0])
    elif S[0] == S[2]:
        print(S[1])
    else:
        print(S[0])

=======
Suggestion 9

def main():
    s = input()
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            print(s[i])
            exit()
    print(-1)

=======
Suggestion 10

def main():
    s = input()
    if len(s) == len(set(s)):
        print(s[0])
    else:
        print(-1)
