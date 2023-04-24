Synthesizing 10/10 solutions (Duplicates hidden)

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
    if not s[1:].replace('C', '').islower():
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
    if s[1:].replace('C', '').islower() == False:
        print('WA')
        return
    print('AC')
    return

=======
Suggestion 3

def main():
    s = input()
    if s[0] != "A":
        print("WA")
        return
    if s[2:-1].count("C") != 1:
        print("WA")
        return
    if s[1:].replace("C", "").islower() == False:
        print("WA")
        return
    print("AC")

=======
Suggestion 4

def main():
    S = input()
    if S[0] == 'A' and S[2:-1].count('C') == 1 and S[1:].replace('C', '').islower():
        print('AC')
    else:
        print('WA')

=======
Suggestion 5

def main():
    S = input()
    if S[0] != "A":
        print("WA")
        return
    if S[2:-1].count("C") != 1:
        print("WA")
        return
    if S[1:].lower() != S[1:]:
        print("WA")
        return
    if S[2:-1].replace("C", "").lower() != S[2:-1].replace("C", ""):
        print("WA")
        return
    print("AC")

=======
Suggestion 6

def main():
    s = input()
    if s[0] == "A" and s[2:-1].count("C") == 1 and s[1:].replace("C", "").islower():
        print("AC")
    else:
        print("WA")

=======
Suggestion 7

def main():
    s = input()
    if s[0] == 'A' and s[2:-1].count('C') == 1 and s[1:].replace('C','').islower():
        print("AC")
    else:
        print("WA")

=======
Suggestion 8

def main():
    s = input()
    if (s[0] == 'A') and (s[2:-1].count('C') == 1) and (s[1:].replace('C', '').islower()):
        print('AC')
    else:
        print('WA')

=======
Suggestion 9

def main():
    S = input()
    if S[0] != 'A':
        print('WA')
        return
    C_count = 0
    for i in range(2, len(S) - 1):
        if S[i] == 'C':
            C_count += 1
    if C_count != 1:
        print('WA')
        return
    for i in range(1, len(S)):
        if i == 1 or i == len(S) - 1:
            if S[i] == 'C':
                print('WA')
                return
        else:
            if S[i].isupper():
                print('WA')
                return
    print('AC')
