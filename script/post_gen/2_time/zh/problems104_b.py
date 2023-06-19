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
    for i in range(len(s)):
        if i == 0 or i == 2:
            continue
        if s[i].isupper():
            print('WA')
            return
    print('AC')

=======
Suggestion 2

def main():
    S = input()
    if S[0] == "A" and S[2:-1].count("C") == 1:
        S = S.replace("A","")
        S = S.replace("C","")
        if S.islower():
            print("AC")
        else:
            print("WA")
    else:
        print("WA")

=======
Suggestion 3

def main():
    S = input()
    if S[0] == "A" and S[2:-1].count("C") == 1 and S[1:].islower():
        print("AC")
    else:
        print("WA")

=======
Suggestion 4

def main():
    s = input()
    if s[0] == 'A' and s[2:-1].count('C') == 1 and s.replace('A', '').replace('C', '').islower():
        print('AC')
    else:
        print('WA')

=======
Suggestion 5

def main():
    s = input()
    if s[0] == 'A' and s[2:-1].count('C') == 1 and s[1:].replace('C', '').islower():
        print('AC')
    else:
        print('WA')

=======
Suggestion 6

def check(s):
    if s[0] != 'A':
        return False
    if s[2:-1].count('C') != 1:
        return False
    for c in s[1:]:
        if c != 'C' and c.isupper():
            return False
    return True

s = input()
print('AC' if check(s) else 'WA')

=======
Suggestion 7

def main():
    s = input()
    if s[0] != "A":
        print("WA")
        return
    if s[2:-1].count("C") != 1:
        print("WA")
        return
    if s[1] == "C" or s[-1] == "C":
        print("WA")
        return
    for i in range(1, len(s)):
        if s[i] != "C" and s[i].isupper():
            print("WA")
            return
    print("AC")

=======
Suggestion 8

def check(s):
    if s[0] != 'A':
        return False
    if s[2:-1].count('C') != 1:
        return False
    for i in range(len(s)):
        if i == 0 or i == 2 or i == len(s) - 1:
            continue
        if s[i] < 'a' or s[i] > 'z':
            return False
    return True

s = input()

=======
Suggestion 9

def check_str(s):
    if s[0] == 'A' and s[2:-1].count('C') == 1 and s[1:].islower():
        return True
    else:
        return False

=======
Suggestion 10

def main():
    s = input()
    if s[0] != 'A':
        print('WA')
        return
    if s[2:-1].count('C') != 1:
        print('WA')
        return
    for i in range(len(s)):
        if i != 0 and i != 1 and i != s.index('C') and s[i].isupper():
            print('WA')
            return
    print('AC')
    return
