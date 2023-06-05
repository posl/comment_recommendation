Synthesizing 10/10 solutions

=======
Suggestion 1

def rotateString(s, t):
    if s == t:
        return 'Yes'
    else:
        for i in range(len(s)):
            s = s[len(s)-1]+s[:len(s)-1]
            if s == t:
                return 'Yes'
        return 'No'

=======
Suggestion 2

def rotate(s):
    return s[1:] + s[0]

=======
Suggestion 3

def main():
    s = input()
    t = input()
    if len(s) == len(t):
        for i in range(len(s)):
            s = s[-1] + s[:-1]
            if s == t:
                print("Yes")
                exit()
        print("No")
    else:
        print("No")

=======
Suggestion 4

def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print('No')
        return 0
    for i in range(len(s)):
        if s == t:
            print('Yes')
            return 0
        else:
            s = s[-1] + s[:-1]
    print('No')

=======
Suggestion 5

def rotate(s):
    s = s[-1] + s[0:-1]
    return s

S = input()
T = input()

for i in range(len(S)):
    S = rotate(S)
    if S == T:
        print('Yes')
        break
else:
    print('No')

=======
Suggestion 6

def main():
    s = input()
    t = input()

    for i in range(len(s)):
        s = s[-1] + s[:-1]
        if s == t:
            print("Yes")
            exit()

    print("No")

=======
Suggestion 7

def rotate_str(s):
    return s[-1] + s[:-1]

=======
Suggestion 8

def rotate_string(s, t):
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        s = s[-1] + s[:-1]
        if s == t:
            return True
    return False

=======
Suggestion 9

def rotateString(s, t):
    if len(s) != len(t):
        return False
    else:
        for i in range(len(s)):
            if s[i:] + s[:i] == t:
                return True
        return False
s = input()
t = input()

=======
Suggestion 10

def rotate(s):
    return s[-1] + s[:-1]
