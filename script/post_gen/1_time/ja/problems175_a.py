Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    if S == "RRR":
        print(3)
    elif S == "RRS" or S == "SRR":
        print(2)
    elif S == "SSS":
        print(0)
    else:
        print(1)

=======
Suggestion 2

def main():
    S = input()
    if S == 'RRR':
        print(3)
    elif S == 'RRS' or S == 'SRR':
        print(2)
    elif S == 'SSS':
        print(0)
    else:
        print(1)

=======
Suggestion 3

def main():
    s = input()
    if s[0] == s[1] == s[2]:
        print(1)
    elif s[0] == s[1] or s[1] == s[2]:
        print(2)
    else:
        print(0)

=======
Suggestion 4

def main():
    s = input()
    if s[0] == s[1] == s[2]:
        print(0)
    elif s[0] != s[1] != s[2]:
        print(1)
    else:
        print(2)

=======
Suggestion 5

def main():
    S = input()
    cnt = 0
    max_cnt = 0
    for i in range(len(S)):
        if S[i] == 'R':
            cnt += 1
            if max_cnt < cnt:
                max_cnt = cnt
        else:
            cnt = 0
    print(max_cnt)

=======
Suggestion 6

def main():
    S = input()
    result = 0
    count = 0
    for i in range(3):
        if S[i] == 'R':
            count += 1
        else:
            result = max(result, count)
            count = 0
    result = max(result, count)
    print(result)

=======
Suggestion 7

def main():
    s = input()
    print(s.count('R'))

=======
Suggestion 8

def main():
    S = input()
    print(S.count("R"))

=======
Suggestion 9

def solve():
    # -*- coding: utf-8 -*-
    s = input()
    print(s.count('R'))

=======
Suggestion 10

def main():
    s = input()
    r = s.split('S')
    print(len(max(r)))
main()
