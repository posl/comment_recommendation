Synthesizing 10/10 solutions (Duplicates hidden)

=======

def main():
    S = input()
    if S[0] != "A":
        print("WA")
        return
    if S[2:-1].count("C") != 1:
        print("WA")
        return
    if S[1:].replace("C", "").islower() == False:
        print("WA")
        return
    print("AC")

=======

def main():
    s = input()
    if s[0] == 'A' and s[2:-1].count('C') == 1 and s[1:].replace('C', '').islower():
        print('AC')
    else:
        print('WA')

=======

def main():
    s = input()
    if s[0] == "A" and s[2:-1].count("C") == 1 and s[1:].replace("C", "").islower():
        print("AC")
    else:
        print("WA")

=======

def main():
    S = input()
    if S[0] == 'A':
        if S[2:-1].count('C') == 1:
            if S[1:].replace('C', '').islower():
                print('AC')
                return
    print('WA')

=======

def check(s):
    if s[0] != "A":
        return False
    if s[2:-1].count("C") != 1:
        return False
    if s[1:].lower() != s[1:]:
        return False
    return True

s = input()

=======

def main():
    S = input()
    if S[0] == 'A' and S[2:-1].count('C') == 1:
        S = S.replace('A', 'a').replace('C', 'c')
        if S.islower():
            print('AC')
        else:
            print('WA')
    else:
        print('WA')

=======

def main():
    s = input()
    if s[0] == 'A' and s[2:-1].count('C') == 1:
        s = s[1:].replace('C', 'c')
        if s.islower():
            print('AC')
            return
    print('WA')

=======

def isAC(string):
    if string[0] != 'A':
        return False
    if string[2:-1].count('C') != 1:
        return False
    for i in range(len(string)):
        if i != 0 and i != 2 and string[i] == 'C':
            continue
        if string[i].isupper():
            return False
    return True

=======

def isAC(S):
    if S[0] != 'A':
        return False
    elif S[1:3].count('C') != 1:
        return False
    elif S[2:].lower() != S[2:]:
        return False
    elif S[1:].lower() != S[1:]:
        return False
    else:
        return True

S = input()
