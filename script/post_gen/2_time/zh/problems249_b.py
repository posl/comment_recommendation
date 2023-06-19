Synthesizing 10/10 solutions

=======
Suggestion 1

def is_lower(letter):
    return letter.lower() == letter

=======
Suggestion 2

def is_wonderful_str(str):
    len_str = len(str)
    if len_str < 2 or len_str > 100:
        return False
    if str.islower() or str.isupper():
        return False
    if str.isalnum():
        return False
    if str.isalpha():
        return True

=======
Suggestion 3

def is_wonderful_string(s):
    s = sorted(s)
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return 'No'
    if 'a' <= s[0] <= 'z' and 'A' <= s[len(s)-1] <= 'Z':
        return 'Yes'
    else:
        return 'No'

=======
Suggestion 4

def is_wonderful_string(s):
    s = list(s)
    s.sort()
    if s[0].islower() and s[-1].isupper():
        return True
    else:
        return False

s = input()

=======
Suggestion 5

def iswonderful(s):
    if len(s) <= 1:
        return False
    if len(s) == 2:
        if s[0].isupper() and s[1].islower():
            return True
        else:
            return False
    if len(s) > 2:
        if s.islower():
            return False
        if s.isupper():
            return False
        if s[0].isupper() and s[1].islower():
            return iswonderful(s[2:])
        if s[0].islower() and s[1].isupper():
            return iswonderful(s[1:])
        if s[0].isupper() and s[1].isupper():
            return iswonderful(s[1:])
        if s[0].islower() and s[1].islower():
            return iswonderful(s[1:])

=======
Suggestion 6

def check(s):
    if not s.islower() and not s.isupper():
        return False
    if not s.islower():
        return False
    if not s.isupper():
        return False
    return True

s = input()
print('Yes' if check(s) else 'No')

=======
Suggestion 7

def main():
    s = input()
    s1 = s.lower()
    if s1 != s and s1.lower() == s:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def check(s):
    if s.islower() or s.isupper():
        return False
    if s.isalpha():
        if s[0].isupper() and s[-1].islower():
            return True
        else:
            return False
    else:
        return False

=======
Suggestion 9

def main():
    s = input()
    if s[0].isupper() and s[1].islower() and s[2:].islower():
        print('Yes')
    else:
        print('No')

=======
Suggestion 10

def main():
    s = input()
    if len(s) < 2 or len(s) > 100:
        print("No")
    elif s.lower() == s or s.upper() == s:
        print("No")
    elif s.isalnum():
        print("Yes")
    else:
        print("No")
