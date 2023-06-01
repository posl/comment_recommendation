Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    if s[0] == 'A' and s[2:-1].count('C') == 1 and s[1:].replace('C', '').islower():
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
    if len(s) < 4:
        print('WA')
        return
    for i in range(len(s)):
        if i == 0 or i == 2 or i == len(s) - 1:
            continue
        if s[i].isupper():
            print('WA')
            return
    print('AC')

=======
Suggestion 3

def main():
    s = input()
    if s[0] == "A" and s[2:-1].count("C") == 1 and s.replace("A","").replace("C","").islower():
        print("AC")
    else:
        print("WA")

=======
Suggestion 4

def judge(s):
    if s[0] == 'A':
        if s[2:-1].count('C') == 1:
            for i in s[1:]:
                if i.isupper():
                    return False
            return True
    return False

=======
Suggestion 5

def main():
    S = input()
    if S[0]=='A' and S[2:-1].count('C')==1 and S[1:].islower():
        print('AC')
    else:
        print('WA')

=======
Suggestion 6

def main():
    s = input()
    if s[0] != 'A':
        print('WA')
        return
    if s[2:-1].count('C') != 1:
        print('WA')
        return
    for i in s:
        if i == 'A' or i == 'C':
            continue
        if i.isupper():
            print('WA')
            return
    print('AC')

=======
Suggestion 7

def main():
    s = input()
    if s[0] == "A" and s[2:-1].count("C") == 1 and s[1:].replace("C", "").islower():
        print("AC")
    else:
        print("WA")

=======
Suggestion 8

def main():
    s = input()
    if s[0] == 'A' and s[2:-1].count('C') == 1:
        for i in range(1, len(s)):
            if s[i] != 'C' and s[i] == s[i].lower():
                continue
            else:
                print('WA')
                break
        else:
            print('AC')
    else:
        print('WA')

=======
Suggestion 9

def main():
    s = input()
    if s[0] == 'A' and s[2:-1].count('C') == 1:
        s = s.replace('A','')
        s = s.replace('C','')
        if s.islower():
            print('AC')
        else:
            print('WA')
    else:
        print('WA')

=======
Suggestion 10

def main():
    s = input()
    if s[0] != 'A':
        print("WA")
        return
    if s[2:-1].count('C') != 1:
        print("WA")
        return
    if s.replace('A', '').replace('C', '').islower():
        print("AC")
        return
    print("WA")
