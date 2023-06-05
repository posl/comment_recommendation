Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    if s[0] == 'A' and s[2:-1].count('C') == 1 and s[1:].replace('C','').islower():
        print('AC')
    else:
        print('WA')

=======
Suggestion 2

def problems104_b():
    s = input()
    if s[0] != 'A':
        print('WA')
        return
    if s[2:-1].count('C') != 1:
        print('WA')
        return
    if s[1:].replace('C','').islower():
        print('AC')
    else:
        print('WA')

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
    if s[2:-1].islower() == False:
        print('WA')
        return
    if s[-1].islower() == False:
        print('WA')
        return
    print('AC')

=======
Suggestion 4

def problem104_b():
    s = input()
    if s[0] != 'A':
        print("WA")
        return
    if s[2:-1].count('C') != 1:
        print("WA")
        return
    for i in range(1,len(s)):
        if s[i] != 'C' and s[i].isupper():
            print("WA")
            return
    print("AC")

=======
Suggestion 5

def main():
    s = input()
    if s[0] != "A":
        print("WA")
        return
    if s[2:-1].count("C") != 1:
        print("WA")
        return
    if s[1:].replace("C","").islower():
        print("AC")
    else:
        print("WA")
main()

=======
Suggestion 6

def solve():
    s = input()
    if s[0] != 'A':
        print('WA')
        return
    if s[2:-1].count('C') != 1:
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
Suggestion 7

def main():
    s = input()
    if s[0] == "A" and s[2:-1].count("C") == 1 and s[1:].islower():
        print("AC")
    else:
        print("WA")

=======
Suggestion 8

def main():
    s = input()
    if s[0] != 'A':
        print('WA')
        return
    if s[2:-1].count('C') != 1:
        print('WA')
        return
    for i in range(1, len(s)):
        if s[i] != 'C' and s[i].isupper():
            print('WA')
            return
    print('AC')

=======
Suggestion 9

def main():
    s=input()
    if s[0]=='A' and s[2:-1].count('C')==1:
        for i in s[1:]:
            if i.isupper():
                print('WA')
                break
        else:
            print('AC')
    else:
        print('WA')

=======
Suggestion 10

def isUpper(s):
    if s.isupper():
        return True
    else:
        return False
