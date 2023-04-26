Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    if s[0::2].islower() and s[1::2].isupper():
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    S = input()
    if S[0::2].islower() and S[1::2].isupper():
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    s = input()
    odd = s[::2]
    even = s[1::2]
    if odd.islower() and even.isupper():
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def check(s):
    odd = s[::2]
    even = s[1::2]
    if odd.islower() and even.isupper():
        return True
    else:
        return False

=======
Suggestion 5

def judge(s):
    if s[0::2].islower() and s[1::2].isupper():
        print('Yes')
    else:
        print('No')

s = input()
judge(s)

=======
Suggestion 6

def check(s):
    if s[0::2].islower() and s[1::2].isupper():
        return True
    else:
        return False

=======
Suggestion 7

def isUpper(s):
    if s.isupper():
        return True
    else:
        return False

=======
Suggestion 8

def is_upper_or_lower(s):
    return s.isupper() or s.islower()

s = input()
