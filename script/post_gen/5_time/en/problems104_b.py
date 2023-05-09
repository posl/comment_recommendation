Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    if s[0] != 'A':
        print('WA')
        return
    if s[2:-1].count('C') != 1:
        print('WA')
        return
    for c in s:
        if c == 'C':
            continue
        if c.isupper():
            print('WA')
            return
    print('AC')

=======
Suggestion 2

def main():
    s = input()
    if s[0] != "A":
        print("WA")
        return
    if s[2:-1].count("C") != 1:
        print("WA")
        return
    for c in s:
        if c not in "AC":
            if c.isupper():
                print("WA")
                return
    print("AC")

=======
Suggestion 3

def main():
    S = input()
    if S[0] != 'A':
        print("WA")
        return
    if S[2:-1].count('C') != 1:
        print("WA")
        return
    for i in range(1, len(S)):
        if S[i] != 'C' and S[i].isupper():
            print("WA")
            return
    print("AC")

=======
Suggestion 4

def main():
    s = input()
    if s[0] == "A" and s[2:-1].count("C") == 1 and s[1:].replace("C", "").islower():
        print("AC")
    else:
        print("WA")

=======
Suggestion 5

def check(s):
    if s[0] != 'A':
        return False
    if s[2:-1].count('C') != 1:
        return False
    for c in s:
        if c != 'A' and c != 'C' and c.isupper():
            return False
    return True

s = input()

=======
Suggestion 6

def main():
    s = input()
    if s[0] == 'A':
        if s[2:-1].count('C') == 1:
            s = s.replace('A', '')
            s = s.replace('C', '')
            if s.islower():
                print('AC')
                return
    print('WA')

=======
Suggestion 7

def main():
    S = input()
    if S[0] == "A" and S[2:-1].count("C") == 1:
        S = S.replace("A", "").replace("C", "")
        if S.islower():
            print("AC")
            return
    print("WA")

=======
Suggestion 8

def main():
    s = input()
    if s[0] == 'A' and s[2:-1].count('C') == 1:
        for i in range(1, len(s)):
            if s[i] != 'C' and s[i].isupper():
                print("WA")
                exit()
        print("AC")
    else:
        print("WA")

=======
Suggestion 9

def main():
    s = input()
    if s[0] == 'A' and s[2:-1].count('C') == 1:
        for i in range(1, len(s)):
            if s[i] == 'C':
                continue
            if s[i].isupper():
                print('WA')
                return
        print('AC')
    else:
        print('WA')

=======
Suggestion 10

def main():
    S = input()
    if S[0] == "A" and S[2:-1].count("C") == 1:
        for i in range(1, len(S)):
            if S[i] == "C":
                continue
            elif S[i].islower():
                continue
            else:
                print("WA")
                return
        print("AC")
    else:
        print("WA")
