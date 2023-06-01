Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    if s[0] == "A":
        if s[2:-1].count("C") == 1:
            if s[1:].replace("C","").islower():
                print("AC")
                return
    print("WA")
    return

=======
Suggestion 2

def solve():
    s = input()
    if s[0] != 'A':
        print('WA')
        return
    if s[2:-1].count('C') != 1:
        print('WA')
        return
    if s[1:].replace('C', '').islower():
        print('AC')
    else:
        print('WA')

=======
Suggestion 3

def solve():
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

=======
Suggestion 4

def check(s):
    if s[0] != 'A':
        return False
    if s[2:-1].count('C') != 1:
        return False
    if s.replace('A', '').replace('C', '').islower():
        return True
    else:
        return False

=======
Suggestion 5

def judge(s):
    if s[0] != 'A':
        return False
    if s[1] != s[-1] != 'C':
        return False
    if s[2:-1].count('C') != 1:
        return False
    for i in s[2:-1]:
        if i != i.lower():
            return False
    return True

=======
Suggestion 6

def is_ac():
    s = input()
    if s[0] == 'A' and 'C' in s[2:-1] and s[1:].islower():
        return 'AC'
    else:
        return 'WA'

=======
Suggestion 7

def main():
    S = input()
    if S[0] != 'A':
        print('WA')
        return
    if S[2:-1].count('C') != 1:
        print('WA')
        return
    for i in range(1, len(S)):
        if S[i] != 'C' and S[i].isupper():
            print('WA')
            return
    print('AC')

=======
Suggestion 8

def test():
    s = input()
    if s[0] != "A":
        print("WA")
        return
    if s[2:-1].count("C") != 1:
        print("WA")
        return
    if s[1:].replace("C", "").islower():
        print("AC")
    else:
        print("WA")

test()

=======
Suggestion 9

def problem104_b():
    s = input()
    if s[0] == 'A' and s[2:-1].count('C') == 1:
        s = s.replace('A', '').replace('C', '')
        if s.islower():
            print('AC')
            return
    print('WA')

=======
Suggestion 10

def main():
    s = input()
    if s[0] == "A":
        if s[2:-1].count("C") == 1:
            for i in s[1:]:
                if i != "C" and i.isupper():
                    print("WA")
                    break
            else:
                print("AC")
        else:
            print("WA")
    else:
        print("WA")
