Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    if S[0] == S[1] == S[2]:
        print(1)
    elif S[0] == S[1] or S[1] == S[2] or S[0] == S[2]:
        print(3)
    else:
        print(6)

=======
Suggestion 2

def main():
    S = input()
    if S[0] == S[1] and S[1] == S[2]:
        print(1)
    elif S[0] == S[1] or S[1] == S[2] or S[0] == S[2]:
        print(3)
    else:
        print(6)

=======
Suggestion 3

def main():
    s = input()
    if s[0] == s[1] == s[2]:
        print(1)
    elif s[0] == s[1] or s[1] == s[2] or s[0] == s[2]:
        print(3)
    else:
        print(6)

=======
Suggestion 4

def main():
    S = input()
    if S[0] == S[1] and S[1] == S[2]:
        print(1)
    elif S[0] == S[1] or S[1] == S[2] or S[2] == S[0]:
        print(3)
    else:
        print(6)

=======
Suggestion 5

def main():
    s = input()
    if s[0] == s[1] and s[1] == s[2]:
        print(1)
    elif s[0] == s[1] or s[1] == s[2] or s[0] == s[2]:
        print(3)
    else:
        print(6)

=======
Suggestion 6

def main():
    s = input()
    if s[0] == s[1] == s[2]:
        print(1)
    elif s[0] == s[1] or s[0] == s[2] or s[1] == s[2]:
        print(3)
    else:
        print(6)

=======
Suggestion 7

def main():
    S = input()
    if S[0] == S[1] and S[1] == S[2]:
        print(1)
    elif S[0] != S[1] and S[1] != S[2] and S[0] != S[2]:
        print(6)
    else:
        print(3)

=======
Suggestion 8

def  main():
    s = input()
    l = list(s)
    l.sort()
    count = 1
    for  i  in  range(0, len(l)-1):
        if  l[i] != l[i+1]:
            count += 1
    print(count)

=======
Suggestion 9

def main():
    S = input()
    print(len(set(S)))
