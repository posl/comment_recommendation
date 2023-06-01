Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    if s.islower() or s.isupper():
        print('No')
    else:
        print('Yes')

=======
Suggestion 2

def is_wonderful_string(s):
    if len(s) < 2 or len(s) > 100:
        return False
    if s.islower() or s.isupper():
        return False
    if s.isalnum():
        return False
    if s.isalpha():
        return True
    return False

=======
Suggestion 3

def check(s):
    if(s.islower() or s.isupper() or len(s)%2!=0):
        return False
    else:
        return True

s=input()
if(check(s)):
    print("Yes")
else:
    print("No")

=======
Suggestion 4

def main():
    s = input()
    if s.islower():
        print('No')
    elif s.isupper():
        print('No')
    elif len(s) == 1:
        print('No')
    elif len(s) == 2:
        if s[0] == s[1]:
            print('No')
        else:
            print('Yes')
    else:
        if s[0] == s[1]:
            print('No')
        elif s[0] == s[-1]:
            print('No')
        elif s[1] == s[-1]:
            print('No')
        else:
            print('Yes')

=======
Suggestion 5

def is_wonderful_string(s):
    if not s.islower() and not s.isupper():
        return False
    if not s.islower():
        if s[0].isupper():
            return True
        else:
            return False
    if not s.isupper():
        if s[0].islower():
            return True
        else:
            return False

s = input()

=======
Suggestion 6

def is_wonderful_string(string):
    if len(string) < 2:
        return False
    if len(string) == 2:
        return string[0] != string[1]
    if len(string) % 2 == 1:
        return False
    if string[0].isupper():
        return False
    if string[-1].islower():
        return False
    if string[0].islower() and string[-1].isupper():
        return False

    return True

=======
Suggestion 7

def check(s):
    if len(s) < 2:
        return False
    if len(s) % 2 != 0:
        return False
    if s[0].isupper() == False:
        return False
    if s[-1].islower() == False:
        return False
    for i in range(1, len(s)-1):
        if i % 2 != 0:
            if s[i].isupper() == True:
                return False
        else:
            if s[i].islower() == True:
                return False
    return True

s = input()

=======
Suggestion 8

def is_wonderful(s):
    if len(s) < 3:
        return False
    if s.islower():
        return False
    if s.isupper():
        return False
    if s.lower() == s.upper():
        return False
    for i in range(0, len(s)):
        if s[i].islower():
            if s[i].upper() not in s[i+1:]:
                return False
        if s[i].isupper():
            if s[i].lower() not in s[i+1:]:
                return False
    return True

=======
Suggestion 9

def main():
    S = input()
    if S.islower() or S.isupper():
        print('No')
    else:
        print('Yes')

=======
Suggestion 10

def is_upper(s):
    return s.isupper()
