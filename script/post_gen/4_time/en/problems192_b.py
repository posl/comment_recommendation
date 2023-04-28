Synthesizing 10/10 solutions

=======
Suggestion 1

def isHardToRead(s):
    for i in range(0, len(s), 2):
        if s[i].islower():
            return False
    for i in range(1, len(s), 2):
        if s[i].isupper():
            return False
    return True

=======
Suggestion 2

def is_hard_to_read(s):
    for i in range(len(s)):
        if i % 2 == 0 and s[i].isupper():
            return False
        if i % 2 == 1 and s[i].islower():
            return False
    return True

=======
Suggestion 3

def solve():
    s = input()
    if s[::2].islower() and s[1::2].isupper():
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    string = input()
    if string[::2].islower() and string[1::2].isupper():
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def isHardToRead(s):
    for i in range(len(s)):
        if i%2 == 0:
            if s[i].isupper() == True:
                return False
        else:
            if s[i].islower() == True:
                return False
    return True

=======
Suggestion 6

def solve():
    s = input()
    for i, c in enumerate(s):
        if i % 2 == 0:
            if c.islower():
                continue
            else:
                return False
        else:
            if c.isupper():
                continue
            else:
                return False
    return True

=======
Suggestion 7

def is_hard_to_read(s):
    for i in range(0, len(s), 2):
        if s[i] != s[i].upper():
            return 'No'
    for i in range(1, len(s), 2):
        if s[i] != s[i].lower():
            return 'No'
    return 'Yes'

s = input()
print(is_hard_to_read(s))

=======
Suggestion 8

def main():
    s=input()
    odd = s[::2]
    even = s[1::2]
    if odd.islower() and even.isupper():
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    s = input()
    if len(s) == 1:
        print("Yes")
        return
    for i in range(0,len(s),2):
        if s[i].islower():
            print("No")
            return
    for i in range(1,len(s),2):
        if s[i].isupper():
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 10

def main():
    S = input()
    #print(S)
    if S[::2].islower() and S[1::2].isupper():
        print('Yes')
    else:
        print('No')
