Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    if S[0] != 'A':
        print('WA')
        return
    if S[2:-1].count('C') != 1:
        print('WA')
        return
    if S[1:].replace('C', '').islower():
        print('AC')
    else:
        print('WA')

=======
Suggestion 2

def main():
    s = input()
    if s[0] != 'A':
        print('WA')
        return
    if s[2:-1].count('C') != 1:
        print('WA')
        return
    if s[1] == 'C' or s[-1] == 'C':
        print('WA')
        return
    for i in range(1, len(s)):
        if s[i] == 'C':
            continue
        if s[i].isupper():
            print('WA')
            return
    print('AC')

main()

=======
Suggestion 3

def main():
    s = input()
    if s[0] != 'A':
        print('WA')
        return
    if s[2:-1].count('C') != 1:
        print('WA')
        return
    if s[1::].islower():
        print('AC')
    else:
        print('WA')

=======
Suggestion 4

def solution(s):
    if s[0]!="A":
        return "WA"
    if "C" not in s[2:-1]:
        return "WA"
    if s[-1]=="C":
        return "WA"
    if s[1:s.index("C")].islower() and s[s.index("C")+1:].islower():
        return "AC"
    return "WA"

=======
Suggestion 5

def main():
    s = input()
    if s[0] == 'A':
        if s[2:-1].count('C') == 1:
            if s[1:].replace('C','').islower():
                print('AC')
                return
    print('WA')

=======
Suggestion 6

def main():
    s = input()
    if s[0] == 'A' and s[2:-1].count('C') == 1:
        for i in range(len(s)):
            if i == 0:
                continue
            elif i == 1:
                if s[i] != 'C':
                    print('WA')
                    exit()
            elif i == len(s) - 1:
                if s[i].isupper():
                    print('WA')
                    exit()
            else:
                if s[i].isupper():
                    print('WA')
                    exit()
        print('AC')
    else:
        print('WA')

=======
Suggestion 7

def solve():
    S = input()
    if S[0] != 'A':
        print('WA')
        return
    if S[2:-1].count('C') != 1:
        print('WA')
        return
    for i in range(1,len(S)):
        if S[i] == 'C':
            continue
        if S[i].isupper():
            print('WA')
            return
    print('AC')

=======
Suggestion 8

def main():
    s = input()
    if s[0] == 'A' and 'C' in s[2:-1] and s.count('C') == 1 and s[1:].islower():
        print('AC')
    else:
        print('WA')

=======
Suggestion 9

def main():
    s = input()
    if s[0] == 'A' and s[2:-1].count('C') == 1:
        if s[1:].replace('C', '').islower():
            print('AC')
            return
    print('WA')

=======
Suggestion 10

def main():
    s = input()
    if s[0] == 'A' and s[2:-1].count('C') == 1 and s[1:].replace('C', '').islower():
        print('AC')
    else:
        print('WA')
