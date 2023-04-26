Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    if s[0] == 'A' and s[2:-1].count('C') == 1 and s[2:-1].islower():
        print('AC')
    else:
        print('WA')

=======
Suggestion 2

def main():
    S = input()
    if S[0] == "A":
        if S[2:-1].count("C") == 1:
            if S.replace("A","").replace("C","").islower():
                print("AC")
                exit()
    print("WA")

=======
Suggestion 3

def main():
    s = input()
    if s[0] == "A" and s[2:-1].count("C") == 1:
        cnt = 0
        for i in range(len(s)):
            if s[i].isupper():
                cnt += 1
        if cnt == 2:
            print("AC")
            return
    print("WA")
    return

=======
Suggestion 4

def main():
    S = input()
    if S[0] == 'A' and S[2:-1].count('C') == 1:
        if S[1:].replace('C', '').islower():
            print('AC')
            return
    print('WA')

=======
Suggestion 5

def is_ac(s):
    if s[0] != 'A':
        return False
    if s[2:-1].count('C') != 1:
        return False
    for i in range(len(s)):
        if i == 0:
            continue
        elif i == 1:
            if s[i] != 'C':
                if s[i].isupper():
                    return False
                else:
                    continue
            else:
                return False
        elif i == len(s)-1:
            if s[i].isupper():
                return False
            else:
                continue
        else:
            if s[i].isupper():
                return False
            else:
                continue
    return True

=======
Suggestion 6

def main():
    S = input()
    if S[0] == 'A' and S[2:-1].count('C') == 1:
        for i in range(1,len(S)):
            if S[i] != 'C' and S[i].isupper():
                print('WA')
                return
        print('AC')
    else:
        print('WA')

=======
Suggestion 7

def check(s):
    if s[0] != "A":
        return False

    if s[2:-1].count("C") != 1:
        return False

    for i in range(len(s)):
        if i == 0:
            continue
        if s[i] == "A":
            continue
        if s[i] == "C":
            continue
        if s[i].islower():
            continue
        return False

    return True

s = input()

=======
Suggestion 8

def main():
    S = input()
    if S[:1] == 'A' and S[2:-1].count('C') == 1 and S[1:].islower():
        print('AC')
    else:
        print('WA')

=======
Suggestion 9

def main():
    s = input()
    if s[0] == "A":
        if s[2:-1].count("C") == 1:
            if s[1:s[2:-1].find("C")+2].islower() and s[s[2:-1].find("C")+3:-1].islower():
                if s[-1].islower():
                    print("AC")
                    exit()
    print("WA")

=======
Suggestion 10

def is_upper_c(s):
    if s.isupper() and s == "C":
        return True
    else:
        return False
