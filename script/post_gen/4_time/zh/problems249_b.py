Synthesizing 10/10 solutions

=======
Suggestion 1

def is_wonderful(s):
    if len(s) < 2:
        return 'No'

    if len(s) == 2:
        if s[0].isupper() and s[1].islower():
            return 'Yes'
        else:
            return 'No'

    for i in range(len(s)):
        if s[i].isupper():
            for j in range(i+1,len(s)):
                if s[j].islower():
                    if s[i].lower() == s[j].lower():
                        return 'Yes'
                    else:
                        return 'No'
    return 'No'

=======
Suggestion 2

def check(s):
    if len(s) < 2 or len(s) > 100:
        print("No")
        return
    if s.islower() or s.isupper():
        print("No")
        return
    if s[0].islower() and s[1].isupper():
        print("Yes")
        return
    if s[0].isupper() and s[1].islower():
        print("Yes")
        return
    for i in range(2, len(s)):
        if s[i].islower() and s[i-1].isupper():
            print("Yes")
            return
        if s[i].isupper() and s[i-1].islower():
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 3

def solve():
    s = input()
    if s.islower() == True:
        print("No")
    elif s.isupper() == True:
        print("No")
    else:
        print("Yes")
solve()

=======
Suggestion 4

def main():
    s = input()
    if s.islower() or s.isupper():
        print("No")
    elif s.isalpha():
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def is_wonderful_string(s):
    if len(s) < 2:
        return False
    if s[0].islower() or s[-1].islower():
        return False
    if s[0].isupper() and s[1].isupper():
        return False
    if s[-1].isupper() and s[-2].isupper():
        return False
    for i in range(1, len(s) - 1):
        if s[i].isupper() and s[i + 1].isupper():
            return False
        if s[i].islower() and s[i + 1].islower():
            return False
    return True

=======
Suggestion 6

def main():
    s = input()
    if s.islower() or s.isupper():
        print('No')
    elif s[0].islower() and s[-1].islower():
        print('No')
    elif s[0].isupper() and s[-1].isupper():
        print('No')
    else:
        print('Yes')

=======
Suggestion 7

def check(s):
    if s.islower():
        return False
    elif s.isupper():
        return False
    elif len(s) % 2 != 0:
        return False
    else:
        for i in range(0, len(s), 2):
            if s[i].islower() or s[i+1].isupper():
                return False
        return True

=======
Suggestion 8

def is_wonderful(s):
    if len(s) < 2:
        return "No"
    if s.islower() or s.isupper():
        return "No"
    if s[0].islower() and s[1].isupper():
        return "No"
    if s[0].isupper() and s[1].islower():
        return "No"
    if s[0].isupper():
        for i in range(1, len(s), 2):
            if s[i].isupper():
                return "No"
            if s[i].islower():
                continue
            else:
                return "No"
    if s[0].islower():
        for i in range(1, len(s), 2):
            if s[i].islower():
                return "No"
            if s[i].isupper():
                continue
            else:
                return "No"
    return "Yes"

=======
Suggestion 9

def main():
    s = input()
    if s.islower() or s.isupper():
        print("No")
    elif s.islower() == False and s.isupper() == False:
        if s.isalpha() == False:
            print("No")
        else:
            if s[0].islower() and s[-1].islower():
                print("No")
            elif s[0].isupper() and s[-1].isupper():
                print("No")
            else:
                print("Yes")

=======
Suggestion 10

def solve():
    s = input()
    if s.islower():
        print('No')
        return
    if s.isupper():
        print('No')
        return
    if len(s) % 2 != 0:
        print('No')
        return
    print('Yes')
