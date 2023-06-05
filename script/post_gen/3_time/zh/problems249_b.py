Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    if s.islower() or s.isupper():
        print("No")
        return
    if s[0].islower() or s[-1].isupper():
        print("No")
        return
    for i in range(1, len(s) - 1):
        if s[i].isupper():
            if s[i + 1].isupper() or s[i - 1].isupper():
                print("No")
                return
        else:
            if s[i + 1].islower() or s[i - 1].islower():
                print("No")
                return
    print("Yes")

=======
Suggestion 2

def main():
    s = input()
    if s.islower():
        print("No")
        exit()
    if s.isupper():
        print("No")
        exit()
    if len(s) % 2 != 0:
        print("No")
        exit()
    if s[0] == s[1]:
        print("No")
        exit()
    if s[-1] == s[-2]:
        print("No")
        exit()
    print("Yes")

=======
Suggestion 3

def main():
    s = input()
    if s.islower():
        print("No")
    elif s.isupper():
        print("No")
    elif len(s) == 1:
        print("No")
    else:
        print("Yes")

=======
Suggestion 4

def main():
    s = input()
    if s.islower() or s.isupper() or len(s) < 2:
        print("No")
        return
    if len(s) % 2 != 0:
        print("No")
        return
    if s[0].islower():
        print("No")
        return
    if s[-1].isupper():
        print("No")
        return
    print("Yes")

=======
Suggestion 5

def check(s):
    if len(s) < 3:
        return False
    if s.islower() or s.isupper():
        return False
    if len(s) % 2 != 0:
        return False
    for i in range(0, len(s), 2):
        if s[i] != s[i+1]:
            return False
    return True

s = input()
print("Yes" if check(s) else "No")

=======
Suggestion 6

def isWonderfulString(s):
    if len(s) < 2:
        return False
    if len(s) == 2:
        if s[0].islower() and s[1].isupper():
            return True
        else:
            return False
    else:
        if s[0].islower() and s[1].isupper():
            for i in range(2, len(s)):
                if s[i].islower() and s[i-2].islower():
                    return False
                if s[i].isupper() and s[i-2].isupper():
                    return False
            return True
        else:
            return False

s = input()

=======
Suggestion 7

def main():
    S = input()
    if S.islower() == False and S.isupper() == False and S.isalnum() == True:
        if len(S) % 2 == 0:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

=======
Suggestion 8

def check(s):
    if len(s) < 2:
        return False
    if s[0].isupper() and s[1].islower():
        return True
    if s[0].islower() and s[1].isupper():
        return True
    return False

s = input()

=======
Suggestion 9

def is_wonderful_string(s):
    if len(s) < 2:
        return False
    if len(s) == 2:
        if s[0].isupper() and s[1].islower():
            return True
        else:
            return False
    if len(s) > 2:
        if s[0].isupper() and s[1].islower():
            for i in range(2, len(s)):
                if s[i].isupper() and s[i-1].islower():
                    return True
                else:
                    continue
        else:
            return False
    return False

=======
Suggestion 10

def main():
    s = input()
    if s.islower():
        print("No")
        return
    if s.isupper():
        print("No")
        return
    if s[0].islower():
        print("No")
        return
    if s[-1].isupper():
        print("No")
        return
    print("Yes")
main()
