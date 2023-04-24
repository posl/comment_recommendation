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
    for i in range(1, len(s)):
        if i == 1:
            continue
        if s[i] == 'C':
            continue
        if s[i].isupper():
            print('WA')
            return
    print('AC')

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
    if s[1:].replace('C','').islower():
        print('AC')
    else:
        print('WA')

=======
Suggestion 3

def main():
    S = input()
    if S[0] != 'A':
        print('WA')
        return
    if S[2:-1].count('C') != 1:
        print('WA')
        return
    if len(S) - S[2:-1].count('C') - S.count('A') != 2:
        print('WA')
        return
    print('AC')

main()

=======
Suggestion 4

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

    for c in s[1:]:
        if c != "C" and c.isupper():
            print("WA")
            return

    print("AC")

=======
Suggestion 5

def main():
    s = input()
    if s[0] == 'A' and s[2:-1].count('C') == 1:
        s = s.replace('A', '').replace('C', '')
        if s.islower():
            print('AC')
            return
    print('WA')

=======
Suggestion 6

def main():
    # input
    S = input()

    # compute

    # output
    if S[0]=='A' and S[2:-1].count('C')==1:
        print('AC')
    else:
        print('WA')

=======
Suggestion 7

def main():
    s = input()
    if s[0] == 'A' and s[2:-1].count('C') == 1:
        if s[1].islower() and s[-1].islower() and s[2:-1].islower():
            print('AC')
            return
    print('WA')

=======
Suggestion 8

def check(s):
    if s[0] != 'A':
        return False
    if s[1:].count('C') != 1:
        return False
    for c in s:
        if c != 'A' and c != 'C':
            if c.isupper():
                return False
    return True

s = input()
print('AC' if check(s) else 'WA')

=======
Suggestion 9

def solve(string):
    if string[0] != 'A':
        return 'WA'
    if string[2:-1].count('C') != 1:
        return 'WA'
    for s in string:
        if s != 'A' and s != 'C' and s.isupper():
            return 'WA'
    return 'AC'

=======
Suggestion 10

def check_problem104b(input):
    if input[0] != "A":
        return False
    if input[2:-1].count("C") != 1:
        return False
    for i in range(1,len(input)):
        if input[i] != "C" and input[i].isupper():
            return False
    return True
