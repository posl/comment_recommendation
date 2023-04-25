Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] == 'L':
                print('No')
                return
        else:
            if s[i] == 'R':
                print('No')
                return
    print('Yes')

=======
Suggestion 2

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
Suggestion 3

def main():
    s = input()
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] == 'L':
                print('No')
                exit()
        else:
            if s[i] == 'R':
                print('No')
                exit()
    print('Yes')

=======
Suggestion 4

def main():
    s = input()
    if (s[0] == 'R' or s[0] == 'U' or s[0] == 'D') and (s[1] == 'L' or s[1] == 'U' or s[1] == 'D'):
        for i in range(2,len(s)):
            if i % 2 == 0:
                if s[i] == 'R' or s[i] == 'U' or s[i] == 'D':
                    pass
                else:
                    print('No')
                    exit()
            else:
                if s[i] == 'L' or s[i] == 'U' or s[i] == 'D':
                    pass
                else:
                    print('No')
                    exit()
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    s = input()
    if (s[0] == 'R' or s[0] == 'U' or s[0] == 'D') and (s[1] == 'L' or s[1] == 'U' or s[1] == 'D'):
        print('No')
    else:
        print('Yes')

=======
Suggestion 6

def main():
    S = input()
    if S[::2].count("L") == 0 and S[1::2].count("R") == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    S = input()
    for i in range(len(S)):
        if i % 2 == 0 and S[i] == "L":
            print("No")
            return
        elif i % 2 == 1 and S[i] == "R":
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 8

def main():
    S = input()
    if S[::2] == 'RUDLUDR':
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def is_easily_playable(s):
    if len(s) % 2 == 0:
        return False
    for i in range(0, len(s), 2):
        if s[i] in ['L', 'U', 'D']:
            pass
        else:
            return False
    for i in range(1, len(s), 2):
        if s[i] in ['R', 'U', 'D']:
            pass
        else:
            return False
    return True

=======
Suggestion 10

def main():
    s = input()
    if (len(s) % 2 == 0):
        if (s[1::2] == "RUD" * (len(s) // 2)):
            print("Yes")
        else:
            print("No")
    else:
        if (s[0::2] == "RUD" * (len(s) // 2) + "R"):
            print("Yes")
        else:
            print("No")
