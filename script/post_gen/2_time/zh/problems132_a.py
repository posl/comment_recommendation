Synthesizing 10/10 solutions

=======
Suggestion 1

def isAllSame(str):
    return str.count(str[0]) == len(str)

=======
Suggestion 2

def main():
    s = input()
    if len(s) != 4:
        print("No")
        return
    else:
        for i in s:
            if s.count(i) != 2:
                print("No")
                return
        print("Yes")

=======
Suggestion 3

def main():
    s = input()
    s = list(s)
    s.sort()
    if s[0] == s[1] and s[2] == s[3] and s[0] != s[2]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    S = input()
    if len(set(S)) == 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    s = input()
    if len(set(s)) == 2 and s.count(s[0]) == 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    s = input()
    if len(s) != 4:
        print("No")
        return
    if len(set(s)) == 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def isTwoChar(s):
    if len(s) != 4:
        return False
    if len(set(s)) != 2:
        return False
    for c in set(s):
        if s.count(c) != 2:
            return False
    return True

=======
Suggestion 8

def main():
    S = input()
    if len(S) != 4:
        print("No")
        return
    for s in S:
        if S.count(s) != 2:
            print("No")
            return
    print("Yes")

=======
Suggestion 9

def main():
    s = input()
    if len(s) == 4 and s.isupper():
        if len(set(s)) == 2:
            print('Yes')
        else:
            print('No')

=======
Suggestion 10

def main():
    s = input()
    if len(s) != 4:
        print("No")
        return
    if len(set(s)) != 2:
        print("No")
        return
    for c in set(s):
        if s.count(c) != 2:
            print("No")
            return
    print("Yes")
