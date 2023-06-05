Synthesizing 10/10 solutions

=======
Suggestion 1

def check_easy(s):
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] == 'L':
                continue
            else:
                return False
        else:
            if s[i] in ('R', 'U', 'D'):
                continue
            else:
                return False

    return True

=======
Suggestion 2

def main():
    s = input()
    for i in range(0, len(s), 2):
        if s[i] == 'L':
            print('No')
            return
    for i in range(1, len(s), 2):
        if s[i] == 'R':
            print('No')
            return
    print('Yes')

=======
Suggestion 3

def check_easy(s):
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] == 'L':
                continue
            else:
                return False
        else:
            if s[i] == 'R':
                continue
            else:
                return False
    return True

=======
Suggestion 4

def easy_to_play(s):
    for i in range(len(s)):
        if (i+1)%2 == 1:
            if s[i] not in ['R','U','D']:
                return False
        else:
            if s[i] not in ['L','U','D']:
                return False
    return True

=======
Suggestion 5

def main():
    s = input()
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] == "L":
                print("No")
                return
        else:
            if s[i] == "R":
                print("No")
                return
    print("Yes")

=======
Suggestion 6

def main():
    s = input()
    if len(s) % 2 == 1:
        print("No")
    else:
        for i in range(len(s)):
            if i % 2 == 0 and s[i] == "L":
                print("No")
                return
            elif i % 2 == 1 and s[i] == "R":
                print("No")
                return
        print("Yes")

=======
Suggestion 7

def main():
    s=input()
    print("Yes" if all([s[i] in "RUD" for i in range(0,len(s),2)]) and all([s[i] in "LUD" for i in range(1,len(s),2)]) else "No")

=======
Suggestion 8

def check(s):
    if len(s) == 1:
        if s[0] == 'L' or s[0] == 'U' or s[0] == 'D':
            return True
        else:
            return False
    else:
        if s[0] == 'R' or s[0] == 'U' or s[0] == 'D':
            return check(s[1:])
        else:
            return False

s = input()

=======
Suggestion 9

def main():
    S = input()
    for i in range(len(S)):
        if i % 2 == 0:
            if S[i] == 'L':
                print('No')
                exit()
        else:
            if S[i] == 'R':
                print('No')
                exit()
    print('Yes')

=======
Suggestion 10

def main():
    s = input()
    if len(s) % 2 == 0:
        for i in range(1, len(s), 2):
            if s[i] == 'R':
                print('No')
                return
        for i in range(0, len(s), 2):
            if s[i] == 'L':
                print('No')
                return
    else:
        for i in range(0, len(s), 2):
            if s[i] == 'R':
                print('No')
                return
        for i in range(1, len(s), 2):
            if s[i] == 'L':
                print('No')
                return
    print('Yes')
