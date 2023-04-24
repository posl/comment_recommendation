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
    if s[1:].replace('C', '').islower() == False:
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
    S = input()
    if S[0] == 'A' and S[2:-1].count('C') == 1 and S[1:].replace('C', '').islower():
        print('AC')
    else:
        print('WA')

=======
Suggestion 4

def main():
    s = input()
    if s[0] == 'A' and s[2:-1].count('C') == 1 and s[1:].lower() == s[1:]:
        print('AC')
    else:
        print('WA')

=======
Suggestion 5

def main():
    s = input()
    if s[0] == 'A' and s[2:-1].count('C') == 1 and s.replace('A','').replace('C','').islower():
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
    if s[1:].lower() != s[1:]:
        return False
    if s[2:-1].lower() != s[2:-1]:
        return False
    return True

s = input()
print('AC' if check(s) else 'WA')

=======
Suggestion 7

def check(s):
    if s[0] != "A":
        return False
    if s[2:-1].count("C") != 1:
        return False
    if s[1:].lower() != s[1:]:
        return False
    if s[2:-1].replace("C", "").lower() != s[2:-1].replace("C", ""):
        return False
    return True

s = input()

=======
Suggestion 8

def check_ac(s):
    if s[0] != 'A':
        return False
    if s[2:-1].count('C') != 1:
        return False
    if not s[1:].replace('C', '').islower():
        return False
    return True
