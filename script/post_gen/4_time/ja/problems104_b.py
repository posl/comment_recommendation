Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
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
    return

=======
Suggestion 2

def main():
    s = input()
    if s[0] == 'A' and s[2:-1].count('C') == 1 and s[1:].replace('C', '').islower():
        print('AC')
    else:
        print('WA')

=======
Suggestion 3

def main():
    s = input()
    if s[0] == "A" and s[2:-1].count("C") == 1 and s[1:].replace("C", "").islower():
        print("AC")
    else:
        print("WA")

=======
Suggestion 4

def main():
    S = input()
    if S[0] == 'A' and S[2:-1].count('C') == 1 and S[1:].islower():
        print('AC')
    else:
        print('WA')

=======
Suggestion 5

def main():
    S = input()
    if S[0] == "A" and "C" in S[2:-1] and S[1:-1].islower():
        print("AC")
    else:
        print("WA")

=======
Suggestion 6

def main():
    s = input()
    if s[0] == "A" and s[2:-1].count("C") == 1 and s[1].islower() and s[3:-1].islower() and s[-1].islower():
        print("AC")
    else:
        print("WA")

=======
Suggestion 7

def main():
    S = input()
    if S[0] != "A":
        print("WA")
        return
    if S[1:].count("C") != 1:
        print("WA")
        return
    if S[2:-1].islower():
        print("AC")
        return
    print("WA")
    return

=======
Suggestion 8

def main():
    S = input()
    if S[0] == "A" and S[2:-1].count("C") == 1:
        if S[1:].replace("C", "").islower():
            print("AC")
        else:
            print("WA")
    else:
        print("WA")

=======
Suggestion 9

def check_ac(s):
    if s[0] != 'A':
        return False
    if s[1] == 'C' or s[-2] == 'C':
        return False
    if s[2:-2].count('C') != 1:
        return False
    for i in s:
        if i != 'A' and i != 'C' and i.isupper():
            return False
    return True

s = input()
