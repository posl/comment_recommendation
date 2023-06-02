Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    if len(s) % 2 == 0:
        for i in range(0, len(s), 2):
            if s[i] == 'L':
                print('No')
                exit()
        for i in range(1, len(s), 2):
            if s[i] == 'R':
                print('No')
                exit()
    else:
        for i in range(0, len(s), 2):
            if s[i] == 'R':
                print('No')
                exit()
        for i in range(1, len(s), 2):
            if s[i] == 'L':
                print('No')
                exit()
    print('Yes')

=======
Suggestion 2

def main():
    S = input()
    for i in range(len(S)):
        if (i % 2 == 0 and S[i] == "L") or (i % 2 == 1 and S[i] == "R"):
            print("No")
            return
    print("Yes")

=======
Suggestion 3

def is_easy_to_play(s):
    if len(s) == 0:
        return False
    for i in range(0, len(s)):
        if i % 2 == 0:
            if s[i] == 'L':
                return False
        else:
            if s[i] == 'R':
                return False
    return True

=======
Suggestion 4

def is_easy(s):
    for i in range(0, len(s), 2):
        if s[i] == 'L':
            return False
    for i in range(1, len(s), 2):
        if s[i] == 'R':
            return False
    return True

=======
Suggestion 5

def main():
    S = input()
    for i in range(0, len(S)):
        if (i % 2 == 0 and S[i] == 'L') or (i % 2 == 1 and S[i] == 'R'):
            print("No")
            return
    print("Yes")

=======
Suggestion 6

def main():
    s = input()
    for i in range(len(s)):
        if i%2==0:
            if s[i] == 'L':
                print('No')
                return
        else:
            if s[i] == 'R':
                print('No')
                return
    print('Yes')

=======
Suggestion 7

def main():
    s = input()
    for i in range(0,len(s)):
        if i % 2 == 0:
            if s[i] == 'L':
                print("No")
                exit()
        else:
            if s[i] == 'R':
                print("No")
                exit()
    print("Yes")

=======
Suggestion 8

def main():
    s = input()
    s1 = s[0::2]
    s2 = s[1::2]
    if s1.count('R') == 0 and s1.count('U') == 0 and s1.count('D') == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def solve():
    S = input()
    if is_easy(S):
        print("Yes")
    else:
        print("No")
